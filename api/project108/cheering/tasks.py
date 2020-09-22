""" Create tasks """

import time
from celery import shared_task
import requests

from .models import Machine
from account.models import User


@shared_task
def run_machine(user_id, machine_id):
    """
    機器を動作させるためのリクエストをこなうためのメソッド
    TODO:どのユーザがリクエストを送ってどの機器を動作させたかの
    記録も行うようにする
    """
    user = User.objects.get(id=user_id)
    machine = Machine.objects.get(id=machine_id)

    path = 'http://{}:8888/raspberry/run'.format(machine.address)
    data = requests.get(path)
