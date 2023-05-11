from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from core import settings

db: SQLAlchemy = SQLAlchemy()


def init_db(app: Flask) -> SQLAlchemy:
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.postgres_dsn
    db.init_app(app)

    return db
