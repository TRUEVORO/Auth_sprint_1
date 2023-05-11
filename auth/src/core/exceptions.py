class AuthError(Exception):
    pass


class UserExistError(AuthError):
    pass


class UserNotExistError(AuthError):
    pass


class WrongPasswordError(AuthError):
    pass


class NoPermissionError(AuthError):
    pass


class EmptyRequestError(AuthError):
    pass
