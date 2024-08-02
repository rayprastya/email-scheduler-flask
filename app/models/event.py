from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    recipients = db.relationship('Recipient', backref='event', lazy=True)
    emails = db.relationship('ScheduledEmail', backref='event', lazy=True)

    def __repr__(self):
        return f'<Event {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'event_name': self.name
        }
