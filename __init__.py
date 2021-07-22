from flask import Flask
from models.models import db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'qwppqpje34jeejejejje12hdhd'

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pashkan:123456@deleteme_db:5432/deleteme"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app
