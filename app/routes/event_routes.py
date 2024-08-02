from flask import Blueprint, request, jsonify, make_response
from app.models.event import Event
from app import db

event_bp = Blueprint('event', __name__, url_prefix='/api/v1/events')

@event_bp.route('', methods=['POST', 'GET'])
def handle_events():
    if request.method == 'POST':
        return create_event()
    elif request.method == 'GET':
        return get_events()
    
def create_event():
    try:
        data = request.get_json()
        new_event = Event(
            name=data['name'],
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully', 'event_id': new_event.id}), 201
    except Exception as e:
        return make_response(jsonify({'message': str(e)}), 500)

def get_events():
    try:
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events]), 200
    except Exception as e:
        return make_response(jsonify({'message': str(e)}), 500)
