from flask import Blueprint, render_template
from app.models.recipient import Recipient
from app import db

template_bp = Blueprint('template', __name__)

@template_bp.route('/')
def index():
    return render_template('index.html')

@template_bp.route('/recipients', methods=['GET'])
def recipients_page():
    return render_template('recipients.html')

@template_bp.route('/events', methods=['GET'])
def events_page():
    return render_template('events.html')

@template_bp.route('/schedule-emails', methods=['GET'])
def schedule_emails_page():
    return render_template('schedule_emails.html')
