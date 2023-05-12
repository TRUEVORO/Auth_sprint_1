from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from clients import sqlalchemy_client
from services import AuthenticationService

auth_routes: Blueprint = Blueprint('auth', __name__, url_prefix='/auth')
auth_service: AuthenticationService = AuthenticationService(client=sqlalchemy_client)


@auth_routes.route('/sign-up', methods=('POST',))
def sign_up():
    """
    Sign Up User
    This endpoint registers a new user with the provided data and returns the created user.
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: user_data
          properties:
            name:
              type: string
              description: The name of the user
            email:
              type: string
              description: The email of the user
            password:
              type: string
              description: The password of the user
    responses:
      200:
        description: User created successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    user_agent = request.headers.get('User-Agent')

    return auth_service.sign_up(request_data, user_agent)


@auth_routes.route('/sign-in', methods=('POST',))
def sign_in():
    """
    Sign In User
    This endpoint authenticates the user with the provided data and returns access and refresh tokens.
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: login_data
          properties:
            email:
              type: string
              description: The email of the user
            password:
              type: string
              description: The password of the user
    responses:
      200:
        description: User authenticated successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    user_agent = request.headers.get('User-Agent')

    return auth_service.sign_in(request_data, user_agent)


@auth_routes.route('/refresh', methods=('POST',))
@jwt_required(refresh=True)
def refresh():
    """
    Refresh Tokens
    This endpoint issues a new pair of access and refresh tokens using the provided refresh token.
    ---
    tags:
      - Authentication
    responses:
      200:
        description: Tokens refreshed successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    return auth_service.refresh()


@auth_routes.route('/sign-out', methods=('POST',))
@jwt_required(refresh=True)
def sign_out():
    """
    Sign Out User
    This endpoint revokes the user's access and refresh tokens and logs them out.
    ---
    tags:
      - Authentication
    responses:
      200:
        description: User signed out successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    return auth_service.sign_out()


@auth_routes.route('/auth-history', methods=('POST',))
@jwt_required()
def auth_history():
    """
    Retrieve user's auth history
    This endpoint retrieves the user's auth history.
    ---
    tags:
      - Authentication
    responses:
      200:
        description: Auth history retrieved successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    return auth_service.auth_history()
