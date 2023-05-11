from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column

from .mixin import UuidMixin, UuidOrmMixin


class RoleName(StrEnum):
    """An enumeration representing user roles."""

    user = 'user'
    admin = 'admin'


class RoleOrm(UuidOrmMixin):
    """Role table."""

    __tablename__ = 'role'

    name: Mapped[RoleName] = mapped_column(unique=True)

    def __repr__(self):
        return f'Role {self.name}'


class Role(UuidMixin):
    """Role model."""

    name: RoleName
