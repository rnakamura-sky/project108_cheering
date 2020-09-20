""" Create tasks """

import time
from celery import shared_task
import requests


@shared_task
def add(x, y):
    """ サンプルのタスク作成 """
    print('処理開始')
    data = requests.get('http://test-worker:8888/raspberry/run')
    print(data.json())
    # time.sleep(3)
    print('処理完了')
    return x + y
