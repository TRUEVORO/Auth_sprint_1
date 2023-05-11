from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from core import settings

jwt: JWTManager = JWTManager()


def init_jwt(app: Flask) -> None:
    app.config['JWT_SECRET_KEY'] = settings.jwt_secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=settings.access_token_expires)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=settings.refresh_token_expires)

    jwt.init_app(app)
