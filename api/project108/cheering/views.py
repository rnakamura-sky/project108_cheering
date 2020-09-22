import datetime
from django.utils import timezone

from django.shortcuts import render, redirect

from celery.result import AsyncResult
from django.contrib import messages
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

        # 入力チェック
        machine_id = request.POST.get('machine', None)
        if not machine_id:
            messages.warning(request, '操作するmachineを選択してください。')
            return redirect('cheering:index')

        machine = Machine.objects.get(id=machine_id)

        group = Group.objects.get(users=user, machines=machine)
        if not group:
            messages.warning(request, '指定されたmachineが存在しない、または操作することができません。')
            return redirect('cheering:index')

        # 回数制限チェック
        day = datetime.date.today()
        count, _ = Count.objects.get_or_create(user=user, date=day)
        if count.count > 10:
            messages.warning(request, '一日に実行できる回数をオーバーしています。')
            state = 'OverCount'
            message = '一日に実行できる回数をオーバーしています。'
        else:
            count.count = count.count + 1
            count.save()
            task_id = run_machine.delay(user.id, machine.id)
            state = 'Recieve'
            message = 'Requestを受け付けました。'

        log = RequestLog(
            state = state,
            user = user,
            machine = machine,
            request_at = timezone.now(),
            message = message
        )
        log.save()

    return redirect('cheering:index')
