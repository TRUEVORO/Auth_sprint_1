from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pydantic import PostgresDsn

db: SQLAlchemy = SQLAlchemy()


def init_db(app: Flask, postgres_dsn: PostgresDsn) -> SQLAlchemy:
    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_dsn
    db.init_app(app)

    return db
