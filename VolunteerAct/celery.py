from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VolunteerAct.settings')

app = Celery('VolunteerAct')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_transport_options={
        'visibility_timeout': 3600,
        'max_connections': 5
    }
)

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
