from django.shortcuts import render, redirect

from django.http import HttpResponse
from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required

from cheering.tasks import run_machine
from cheering.models import Machine
from cheering.models import Group
# Create your views here.


@login_required
def index(request):
    """ ユーザーがメインで使用するページ表示　"""
    user = request.user
    groups = Group.objects.filter(users=user)

    context = {
        'user': user,
        'groups': groups
    }
    return render(request, 'cheering/index.html', context)

@login_required
def call(request):
    print('HELLO')
    if request.POST:
        machine_id = request.POST['machine']
        machine = Machine.objects.get(id=machine_id)
        task_id = run_machine.delay(1, machine.pk)
    return redirect('cheering:index')