import os
from celery import Celery

settings = os.getenv('DJANGO_SETTINGS_MODULE', 'project108.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

app = Celery('project108')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
