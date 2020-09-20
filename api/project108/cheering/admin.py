from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Machine)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(Count)
admin.site.register(RequestLog)
admin.site.register(MachineOperation)
