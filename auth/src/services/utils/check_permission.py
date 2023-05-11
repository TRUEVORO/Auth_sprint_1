from functools import wraps

from flask import Response
from flask_jwt_extended import get_jwt_identity

from core import NoPermissionError


def check_permission(role: str):
    """
    Function to check user permissions.

    :return: results of the func or permission error
    """

    def func_wrapper(func: callable):
        @wraps(func)
        def inner(*args, **kwargs) -> Response | Exception:
            if role not in get_jwt_identity().get('user_roles'):
                raise NoPermissionError('Permission denied')
            return func(*args, **kwargs)

        return inner

    return func_wrapper
