from uuid import UUID

from flask import Response, jsonify

from core import EmptyRequestError
from models import Role, RoleOrm, User, UserOrm

from .base_service import BaseService
from .utils import check_permission, error_handler


class RoleManagerService(BaseService):
    """Role manager service."""

    @error_handler()
    @check_permission('admin')
    def create_role(self, name: str | None = None) -> Response | EmptyRequestError:
        """Create role and add it to database."""

        if not name:
            raise EmptyRequestError('Missing role name')

        role = self.client.create(RoleOrm, name)
        return jsonify('Role {} created!'.format(Role.from_orm(role).dict()))

    @error_handler()
    @check_permission('admin')
    def retrieve_roles(self) -> Response:
        """Retrieve all roles from database."""

        roles = self.client.retrieve(RoleOrm, fetch_all=True)
        return jsonify('Roles: {}'.format([Role.from_orm(role).dict() for role in roles]))

    @error_handler()
    @check_permission('admin')
    def update_role(self, role_id: UUID | None = None, new_name: str | None = None) -> Response:
        """Update name of specific role."""

        if not any((role_id, new_name)):
            raise EmptyRequestError('Missing data')

        role = self.client.update(RoleOrm, uuid=role_id, name=new_name)
        return jsonify('Role {} updated'.format(Role.from_orm(role).dict()))

    @error_handler()
    @check_permission('admin')
    def delete_role(self, role_id: UUID) -> Response:
        """Delete role from database."""

        if not role_id:
            raise EmptyRequestError('Missing role id')

        role = self.client.delete(RoleOrm, uuid=role_id)
        return jsonify('Role {} deleted'.format(Role.from_orm(role).dict()))


class AdminService(RoleManagerService):
    """Admin service."""

    @error_handler()
    @check_permission('admin')
    def assign_user_role(self, user_id: UUID, role_name: str) -> Response:
        """Assign new role to specific user."""

        role = self.client.retrieve(RoleOrm, name=role_name)
        user_role = self.client.retrieve(UserOrm, uuid=user_id).roles
        user = self.client.update(UserOrm, uuid=user_id, role=user_role.append(role))

        return jsonify('Role {} assigned to {}'.format(role_name, User.from_orm(user).dict()))

    @error_handler()
    @check_permission('admin')
    def remove_user_role(self, user_id: UUID, role_name: str) -> Response:
        """Remove role from specific user."""

        role = self.client.retrieve(RoleOrm, name=role_name)
        user_role = self.client.retrieve(UserOrm, uuid=user_id).roles
        user = self.client.update(UserOrm, uuid=user_id, role=user_role.remove(role))

        return jsonify('Role {} removed from {}'.format(role_name, User.from_orm(user).dict()))
