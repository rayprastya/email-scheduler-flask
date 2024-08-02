from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from .config import Config
from .tasks.make_celery import make_celery

from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    with app.app_context():
        from .routes.email_routes import email_bp
        from .routes.event_routes import event_bp
        from .routes.recipient_routes import recipient_bp
        from .routes.template_routes import template_bp
        app.register_blueprint(email_bp)
        app.register_blueprint(event_bp)
        app.register_blueprint(recipient_bp)
        app.register_blueprint(template_bp)
        from . import models 

    return app

def create_celery_app(app=None):
    app = app or create_app()
    celery = make_celery(app)
    celery.conf.update(app.config)
    return celery
