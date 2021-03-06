import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'syms_marketplace.settings')

app = Celery('syms_marketplace')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
     enable_utc=True,
     timezone='Europe/Kiev',
)
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass


@app.task
def get_test_task():
    pass
