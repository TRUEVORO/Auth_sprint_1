from datetime import datetime
from uuid import UUID

from pydantic import Field
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .mixin import UuidMixin, UuidOrmMixin


class AuthHistoryOrm(UuidOrmMixin):
    """User's auth history table."""

    __tablename__ = 'auth_history'

    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    user_agent: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)


class AuthHistory(UuidMixin):
    """User's auth history model."""

    user_id: UUID
    user_agent: str
    timestamp: datetime = Field(default=datetime.now())
