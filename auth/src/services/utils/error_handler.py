from functools import wraps
from http import HTTPStatus

from flask import Response, jsonify
from pydantic import ValidationError

from core import EmptyRequestError, NoPermissionError, UserExistError, UserNotExistError, WrongPasswordError


def error_handler():
    """
    Function for handling request errors.

    :return: results of the search or HTTPException
    """

    def func_wrapper(func: callable):
        @wraps(func)
        def inner(*args, **kwargs) -> tuple[Response, HTTPStatus]:
            try:
                result = func(*args, **kwargs)
            except (EmptyRequestError, UserNotExistError, WrongPasswordError, ValidationError) as e:
                return jsonify({'error': f'{e}'}), HTTPStatus.NOT_FOUND
            except (UserExistError, NoPermissionError) as e:
                return jsonify({'error': f'{e}'}), HTTPStatus.CONFLICT

            return result, HTTPStatus.OK

        return inner

    return func_wrapper
