from app import db
from datetime import datetime
import pytz

class ScheduledEmail(db.Model):
    __tablename__ = 'scheduled_email'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    email_subject = db.Column(db.String(255), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    is_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Singapore')))
    updated_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Singapore')), onupdate=datetime.now(pytz.timezone('Asia/Singapore')))
    deleted_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), default='active')

    def __repr__(self):
        return f'<ScheduledEmail {self.email_subject}>'

    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'email_subject': self.email_subject,
            'email_content': self.email_content,
            'timestamp': self.timestamp.isoformat(),
            'is_sent': self.is_sent,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
            'status': self.status
        }