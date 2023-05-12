from pydantic import EmailStr, Field
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .auth_history import AuthHistory, AuthHistoryOrm
from .mixin import UuidMixin, UuidOrmMixin
from .role import Role, RoleOrm
from .user_role import user_role


class UserOrm(UuidOrmMixin):
    """User table."""

    __tablename__ = 'user'

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    roles: Mapped[list[RoleOrm]] = relationship(secondary=user_role)
    auth_history: Mapped[list[AuthHistoryOrm]] = relationship()

    def __repr__(self):
        return f'<User {self.email}>'


class _User(UuidMixin):
    """Base user model."""

    email: EmailStr
    password: str = Field(min_length=8)


class User(_User):
    """User model."""

    roles: list[Role] = Field(default_factory=list)
    auth_history: list[AuthHistory] = Field(default_factory=list)

    def get_roles(self) -> list[str]:
        """Get user roles."""

        return [role.name for role in self.roles]
