import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

app = Celery('task_manager', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'check_and_log_completed_tasks': {
        'task': 'tasks.tasks.check_and_log_completed_tasks',
        'schedule': crontab(minute='*'),  # Runs every minute (adjust as needed)
    },
}