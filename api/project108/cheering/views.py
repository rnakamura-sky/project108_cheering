from django.utils import timezone
import datetime

from django.shortcuts import render, redirect

from django.http import HttpResponse
from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required

from cheering.tasks import run_machine
from cheering.models import Machine
from cheering.models import Group
from cheering.models import RequestLog
from cheering.models import Count
# Create your views here.


@login_required
def index(request):
    """ ユーザーがメインで使用するページ表示　"""
    user = request.user
    groups = Group.objects.filter(users=user)

    latest_logs = RequestLog.objects.filter(user=user).order_by('-request_at')[:10]

    date = datetime.date.today()
    count = Count.objects.get_or_create(user=user, date=date)[0]
    context = {
        'user': user,
        'count': count,
        'groups': groups,
        'latest_logs': latest_logs,
    }
    return render(request, 'cheering/index.html', context)

@login_required
def call(request):
    if request.POST:
        user = request.user
        machine_id = request.POST['machine']
        machine = Machine.objects.get(id=machine_id)
        log = RequestLog(
            state = 'Request',
            user = user,
            machine = machine,
            request_at = timezone.now(),
            message = 'Requestを受け付けました。'
        )
        log.save()
        day = datetime.date.today()
        count = Count.objects.get_or_create(user=user, date=day)[0]
        count.count = count.count + 1
        count.save()
        task_id = run_machine.delay(user.id, machine.id)
    return redirect('cheering:index')
