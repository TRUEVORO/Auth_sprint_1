from bcrypt import checkpw, gensalt, hashpw
from pydantic import root_validator, validator

from clients import sqlalchemy_client
from core import UserExistError, UserNotExistError, WrongPasswordError

from .user import User, UserOrm, _User


class UserRequest(_User):
    """User request model."""

    user: User | None = None


class LoginRequest(UserRequest):
    """User login request model."""

    @root_validator()
    def check_user(cls, values: dict) -> dict:
        """Validate and return user."""

        email: str = values.get('email')
        password: str = values.get('password')

        user: UserOrm = sqlalchemy_client.retrieve(UserOrm, email=email)

        if not user:
            raise UserNotExistError('user with this email - {} is not exist'.format(email))

        if not checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise WrongPasswordError('passwords do not match')

        values['user']: User = User.from_orm(user)
        return values


class SignupRequest(UserRequest):
    """User signup request model."""

    @validator('email')
    def validate_email(cls, v: str) -> str:
        """Validate provided email."""

        if sqlalchemy_client.retrieve(UserOrm, email=v):
            raise UserExistError('user with this email - {} already exists'.format(v))
        return v

    @validator('password')
    def hash_password(cls, v: str) -> str:
        """Hash password."""

        return hashpw(v.encode('utf-8'), gensalt()).decode('utf-8')

    @validator('user', pre=True, always=True)
    def set_user(cls, v: User | None, values: dict) -> User:
        """Set user."""
        if not v:
            v: User = User(**values)
        return v
