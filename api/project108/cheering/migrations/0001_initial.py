# Generated by Django 3.1.1 on 2020-09-20 02:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('type', models.IntegerField(choices=[(0, 'Private'), (1, 'Public')], verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('unique_id', models.CharField(max_length=20, unique=True, verbose_name='unique_id')),
                ('state', models.IntegerField(choices=[(-1, 'Uninit'), (1, 'Running'), (2, 'Stopped')], verbose_name='state')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('time', models.IntegerField(verbose_name='time')),
                ('music', models.CharField(max_length=100, verbose_name='music')),
                ('interval', models.FloatField(verbose_name='interval')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(verbose_name='priority')),
                ('enable', models.BooleanField(verbose_name='enable')),
                ('start_time', models.TimeField(default=datetime.time(0, 0), verbose_name='start_time')),
                ('end_time', models.TimeField(default=datetime.time(0, 0), verbose_name='ent_time')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheering.group')),
            ],
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_at', models.DateTimeField(verbose_name='request_at')),
                ('state', models.CharField(max_length=20, verbose_name='state')),
                ('message', models.CharField(max_length=200, verbose_name='message')),
                ('machine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cheering.machine')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MachineOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_at', models.DateTimeField(verbose_name='request_at')),
                ('state', models.IntegerField(choices=[(1, 'Request'), (2, 'Execute'), (3, 'Sync'), (4, 'Failed'), (10, 'Complete')])),
                ('machine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cheering.machine')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='machines',
            field=models.ManyToManyField(related_name='groups_machines', to='cheering.Machine'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_name='groups_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date_time')),
                ('count', models.IntegerField(verbose_name='count')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
