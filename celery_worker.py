from app.tasks.email_tasks import celery

if __name__ == '__main__':
    celery.start()
