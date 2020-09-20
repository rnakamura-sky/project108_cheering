from django.shortcuts import render

from django.http import HttpResponse
from celery.result import AsyncResult

from cheering.tasks import add
# Create your views here.

def hello(request):
    """ テスト用メソッド """
    task_id = add.delay(2, 3)
    result = AsyncResult(task_id)
    print('result', result, ' : ', result.state, ' : ', result.ready())
    return HttpResponse('Hello World!')
