from app import create_app, db, mail 
from app.models.email import ScheduledEmail
from app.models.event import Event
from flask_mail import Message
from .make_celery import make_celery
from datetime import datetime
import pytz

app = create_app()
celery = make_celery(app)

@celery.task
def send_scheduled_email(email_id):
    with app.app_context():
        email = ScheduledEmail.query.get(email_id)
        if email:
            singapore_tz = pytz.timezone('Asia/Singapore')
            current_time = datetime.now(singapore_tz)
            
            email_timestamp = email.timestamp.astimezone(singapore_tz) if email.timestamp else None

            if email_timestamp and current_time >= email_timestamp and not email.is_sent:
                recipients = [r.email for r in Event.query.get(email.event_id).recipients]

                if recipients:
                    print("sender", app.config['MAIL_USERNAME'])
                    msg = Message(
                        subject=email.email_subject,
                        sender=app.config['MAIL_USERNAME'],
                        recipients=recipients,
                        body=email.email_content
                    )
                    mail.send(msg)

                    print(f'Sending email: {email.email_subject} to event ID {email.event_id}')
                    email.is_sent = True
                    email.status = 'deactive'
                    email.updated_at = datetime.now(singapore_tz)
                    db.session.commit()
                else:
                    print(f'No recipients found for event ID {email.event_id}.')

            else:
                print(f'Email scheduled for {email_timestamp}, current time is {current_time}. Not sending yet.')
