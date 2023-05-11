from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db


class UuidOrmMixin(db.Model):
    """UUID ORM mixin model."""

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, nullable=False)


class OrmMixin(BaseModel):
    """Orm mixin model."""

    class Config:
        orm_mode = True


class UuidMixin(OrmMixin):
    """UUID mixin model."""

    id: UUID = Field(default_factory=uuid4)
