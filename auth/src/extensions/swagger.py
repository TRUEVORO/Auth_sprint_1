from flasgger import Swagger
from flask import Flask

swagger = Swagger()


def init_swagger(app: Flask) -> None:
    swagger.init_app(app)
