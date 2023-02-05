from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from shared.settings.config import DB_URI, DB_DRIVER_ECHO
from shared.database.metadata import Base

db = SQLAlchemy(metadata=Base.metadata)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = DB_DRIVER_ECHO
    db.init_app(app)
    return app
