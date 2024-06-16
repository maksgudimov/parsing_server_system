import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')


# Автоматическое обнаружение задач во всех установленных приложениях
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'parsing_magnit': {
        'task': 'parsing.tasks.parsing_magnit',
        'schedule': crontab(minute=0, hour=7),
    },
    'parsing_crossroads': {
        'task': 'parsing.tasks.parsing_crossroads',
        'schedule': crontab(minute=5, hour=7),
    },
}
