from flask import Blueprint, request, jsonify, make_response
from app.models.recipient import Recipient
from app import db

recipient_bp = Blueprint('recipient', __name__, url_prefix='/api/v1/recipients')

@recipient_bp.route('', methods=['POST', 'GET'])
def handle_events():
    if request.method == 'POST':
        return create_recipient()
    elif request.method == 'GET':
        return get_recipients()
    
def create_recipient():
    try:
        data = request.get_json()
        new_recipient = Recipient(
            email=data['email'],
            event_id=data['event_id']
        )
        db.session.add(new_recipient)
        db.session.commit()
        return jsonify({'message': 'Recipient created successfully', 'recipient_id': new_recipient.id}), 201
    except Exception as e:
        return make_response(jsonify({'message': str(e)}), 500)

def get_recipients():
    try:
        recipients = Recipient.query.all()
        return jsonify([recipient.to_dict() for recipient in recipients]), 200
    except Exception as e:
        return make_response(jsonify({'message': str(e)}), 500)
