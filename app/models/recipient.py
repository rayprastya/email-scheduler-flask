from app import db

class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __repr__(self):
        return f'<Recipient {self.email}>'

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'event_id': self.event_id
        }