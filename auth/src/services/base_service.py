from abc import ABC
from time import time
from uuid import UUID

from flask_jwt_extended import create_access_token, create_refresh_token, get_jti, get_jwt

from clients import BaseClient
from core import settings
from extensions import jwt, redis_storage
from storages import BaseStorage


class BaseService(ABC):
    """Base service class."""

    jwt_blocklist: BaseStorage = redis_storage

    def __init__(self, client: BaseClient):
        """Initialize BaseService with a client and JWT blocklist storage."""

        self.client: BaseClient = client

    @staticmethod
    @jwt.token_in_blocklist_loader
    def is_invalid_token(jwt_header: dict, jwt_payload: dict) -> bool:  # noqa
        """Check if JWT token is invalid (expired or not in blocklist)."""

        if jwt_payload.get('exp') < time():
            return True

        jti = jwt_payload.get('jti')

        if not jti:
            return True

        return BaseService.jwt_blocklist.retrieve_data(jti) is not None

    def _create_tokens(self, user_id: UUID, user_roles: list[str], is_fresh: bool = False) -> dict[str, str]:  # noqa
        """Create access and refresh tokens."""

        identity = {'user_id': user_id, 'user_roles': user_roles}

        access_token = create_access_token(identity=identity, fresh=is_fresh)
        refresh_token = create_refresh_token(identity=identity, additional_claims={'access_jti': get_jti(access_token)})

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def _revoke_tokens(self) -> None:
        """Revoke access and refresh tokens, should be called in a method decorated with @jwt_required(refresh=True)."""

        payload = get_jwt()
        refresh_jti, refresh_exp = payload.get('jti'), payload.get('exp')
        access_jti = payload.get('access_jti')

        self.jwt_blocklist.save_data(refresh_jti, 'refresh', ttl=int(refresh_exp - time()))
        self.jwt_blocklist.save_data(access_jti, 'access', ttl=settings.access_token_expires)
