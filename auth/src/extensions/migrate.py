from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate: Migrate = Migrate()


def init_migrate(app: Flask, db: SQLAlchemy) -> None:
    migrate.init_app(app, db)
