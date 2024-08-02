from celery import Celery
from celery.schedules import crontab

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(
        result_backend=app.config['CELERY_RESULT_BACKEND'],
        beat_schedule={
            'check-and-send-emails-every-minute': {
                'task': 'app.tasks.email_tasks.check_and_send_emails',
                'schedule': crontab(minute='*')
            }
        }
    )

    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super(ContextTask, self).__call__(*args, **kwargs)

    celery.Task = ContextTask
    return celery
