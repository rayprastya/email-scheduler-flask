import pytest
from app import create_app, db
from app.models import Recipient, Event, ScheduledEmail

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture(scope='module')
def init_database():
    event = Event(name="Test Event")
    recipient = Recipient(email="test@example.com", event_id=event.id)
    db.session.add(event)
    db.session.add(recipient)
    db.session.commit()
    yield db
    db.session.remove()
    db.drop_all()
