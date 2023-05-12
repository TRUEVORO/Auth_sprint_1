from flask import Response, jsonify
from flask_jwt_extended import get_jwt_identity

from models import AuthHistoryOrm, LoginRequest, RoleOrm, SignupRequest, User, UserOrm

from .base_service import BaseService
from .utils import error_handler


class AuthenticationService(BaseService):
    """Authentication service."""

    @error_handler()
    def sign_up(self, request_data: dict, user_agent: str) -> Response:
        """Sign up method."""

        user = SignupRequest(**request_data).user
        base_role = self.client.retrieve(RoleOrm, name='user')

        self.client.create(UserOrm, **user.dict(exclude={'auth_history', 'roles'}), roles=[base_role])
        self.client.create(AuthHistoryOrm, user_id=user.id, user_agent=user_agent)

        return jsonify(self._create_tokens(user.id, [base_role.name], is_fresh=True))

    @error_handler()
    def sign_in(self, request_data: dict, user_agent: str) -> Response:
        """Sign in method."""

        user = LoginRequest(**request_data).user

        self.client.create(AuthHistoryOrm, user_id=user.id, user_agent=user_agent)

        return jsonify(self._create_tokens(user.id, user.get_roles(), is_fresh=True))

    @error_handler()
    def refresh(self) -> Response:
        """Refresh method."""

        user = get_jwt_identity()

        self._revoke_tokens()

        return jsonify(self._create_tokens(user.get('user_id'), user.get('user_roles')))

    @error_handler()
    def sign_out(self) -> Response:
        """Sign out method."""

        self._revoke_tokens()
        return jsonify('signed out')

    @error_handler()
    def auth_history(self) -> Response:
        """Sign out method."""

        user = get_jwt_identity()

        auth_history = User.from_orm(self.client.retrieve(UserOrm, id=user.get('user_id'))).auth_history
        return jsonify([auth.dict(include={'user_agent', 'timestamp'}) for auth in auth_history])
