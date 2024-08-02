from flask import Blueprint, request, jsonify, make_response
from app.models.email import ScheduledEmail
from app.models.event import Event
from app import db
from datetime import datetime
import pytz

email_bp = Blueprint('scheduledemail', __name__, url_prefix='/api/v1')

@email_bp.route('/schedule-emails', methods=['POST', 'GET'])
def handle_emails():
    if request.method == 'POST':
        return save_emails()
    elif request.method == 'GET':
        return get_emails()

def save_emails():
    try:
        data = request.get_json()
        event_id = data['event_id']
        
        event = Event.query.get(event_id)
        if not event:
            return make_response(jsonify({'message': 'Event not found'}), 404)

        recipients = [r.email for r in event.recipients]
        if not recipients:
            return make_response(jsonify({'message': 'No recipients found for this event'}), 404)

        
        timestamp_str = data['timestamp']
        timestamp = datetime.fromisoformat(timestamp_str).astimezone(pytz.timezone('Asia/Singapore'))
        
        email = ScheduledEmail(
            event_id=data['event_id'], 
            email_subject=data['email_subject'], 
            email_content=data['email_content'], 
            timestamp=timestamp
        )
        db.session.add(email)
        db.session.commit()

        from app.tasks.email_tasks import send_scheduled_email
        send_scheduled_email.apply_async(args=[email.id], eta=timestamp)

        return jsonify({'message': 'Email scheduled successfully'}), 201
    except Exception as e:
        return make_response(jsonify({'message': 'error saving emails'}), 500)

def get_emails():
    try:
        emails = ScheduledEmail.query.all()
        return make_response(jsonify([email.to_dict() for email in emails]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting emails'}), 500)

@email_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test route is working!'}), 200
