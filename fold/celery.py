import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fold.settings')

app = Celery('fold')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'log-every-5-minute': {
        'task': 'api.tasks.write_to_logs',
        'schedule': crontab(minute='*/5'),
    }
}
