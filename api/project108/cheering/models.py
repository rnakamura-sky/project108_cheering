from django.db import models
import datetime

from account.models import User
# Create your models here.

class Machine(models.Model):
    class State(models.IntegerChoices):
        UNINIT = -1
        RUNNING = 1
        STOPPED = 2

    name = models.CharField('name', max_length=100)
    unique_id = models.CharField('unique_id', max_length=20, unique=True, null=False)
    state = models.IntegerField('state', choices=State.choices)
    address = models.CharField('address', max_length=100)
    time = models.IntegerField('time')
    music = models.CharField('music', max_length=100)
    interval = models.FloatField('interval')

class Group(models.Model):

    class GroupType(models.IntegerChoices):
        PRIVATE = 0
        PUBLIC = 1

    name = models.CharField('name', max_length=100)
    type = models.IntegerField('type', choices=GroupType.choices)

    users = models.ManyToManyField(User, related_name='groups_users')
    machines = models.ManyToManyField(Machine, related_name='groups_machines')

class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    priority = models.IntegerField('priority')
    enable = models.BooleanField('enable')
    start_time = models.TimeField('start_time', default=datetime.time(0, 0, 0))
    end_time = models.TimeField('ent_time', default=datetime.time(0, 0, 0))

class Count(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('date_time', null=False)
    count = models.IntegerField('count')

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    request_at = models.DateTimeField('request_at')
    state = models.CharField('state', max_length=20)
    message = models.CharField('message', max_length=200)


class MachineOperation(models.Model):
    class State(models.IntegerChoices):
        REQUEST = 1
        EXECUTE = 2
        SYNC = 3
        FAILED = 4
        COMPLETE = 10
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    request_at = models.DateTimeField('request_at')
    state = models.IntegerField(choices=State.choices)
