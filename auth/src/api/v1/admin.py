from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from clients import sqlalchemy_client
from services import AdminService
from services.utils import check_permission

admin_routes: Blueprint = Blueprint('admin', __name__, url_prefix='/admin')
admin_service: AdminService = AdminService(client=sqlalchemy_client)


@admin_routes.route('/roles/create', methods=('POST',))
@jwt_required()
@check_permission('admin')
def create_role():
    """
    Create a new role
    ---
    tags:
      - Admin
    parameters:
      - in: body
        name: body
        schema:
          id: RoleData
          required:
            - name
          properties:
            name:
              type: string
              description: The name of the role.
    responses:
      200:
        description: Role created successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    return admin_service.create_role(request_data.get('name'))


@admin_routes.route('/roles/retrieve_roles', methods=('POST',))
@jwt_required()
@check_permission('admin')
def retrieve_roles():
    """
    Retrieve all roles
    ---
    tags:
      - Admin
    responses:
      200:
        description: Roles retrieved successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    return admin_service.retrieve_roles()


@admin_routes.route('/roles/update_role', methods=('POST',))
@jwt_required()
@check_permission('admin')
def update_role():
    """
    Update a role
    ---
    tags:
      - Admin
    parameters:
      - in: body
        name: body
        schema:
          id: RoleUpdateData
          required:
            - role_id
            - name
          properties:
            role_id:
              type: string
              description: The ID of the role to update.
            name:
              type: string
              description: The new name of the role.
    responses:
      200:
        description: Role updated successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    return admin_service.update_role(request_data.get('role_id'), request_data.get('name'))


@admin_routes.route('/roles/delete_role', methods=('POST',))
@jwt_required()
@check_permission('admin')
def delete_role():
    """
    Delete a role
    ---
    tags:
      - Admin
    parameters:
      - in: body
        name: body
        schema:
          id: RoleDeleteData
          required:
            - role_id
          properties:
            role_id:
              type: string
              description: The ID of the role to delete.
    responses:
      200:
        description: Role deleted successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    return admin_service.delete_role(request_data.get('role_id'))


@admin_routes.route('/assign_role', methods=('POST',))
@jwt_required()
@check_permission('admin')
def assign_user_role():
    """
    Assign a role to a user
    ---
    tags:
      - Admin
    parameters:
      - in: body
        name: body
        schema:
          id: RoleAssignmentData
          required:
            - role_id
            - name
          properties:
            role_id:
              type: string
              description: The ID of the role to assign.
            name:
              type: string
              description: The name of the user to assign the role to.
    responses:
      200:
        description: Role assigned successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    return admin_service.assign_user_role(request_data.get('role_id'), request_data.get('name'))


@admin_routes.route('/remove_role', methods=('POST',))
@jwt_required()
@check_permission('admin')
def remove_user_role():
    """
    Remove a role from a user
    ---
    tags:
      - Admin
    parameters:
      - in: body
        name: body
        schema:
          id: RoleRemovalData
          required:
            - role_id
            - name
          properties:
            role_id:
              type: string
              description: The ID of the role to remove.
            name:
              type: string
              description: The name of the user to remove the role from.
    responses:
      200:
        description: Role removed successfully
      400:
        description: Not found
      409:
        description: Conflict
    """
    request_data = request.get_json()
    return admin_service.remove_user_role(request_data.get('role_id'), request_data.get('name'))
