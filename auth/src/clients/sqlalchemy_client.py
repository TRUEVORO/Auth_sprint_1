from uuid import UUID

from extensions import db

from .base_client import BaseClient


class SQLAlchemyClient(BaseClient):
    """Client for SQLAlchemy providing CRUD operations on database models."""

    def create(self, model: type[db.Model], **kwargs) -> db.Model:
        """Create and return a new instance of the given model."""

        instance = model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def retrieve(self, model: type[db.Model], fetch_all: bool = False, **kwargs) -> db.Model:
        """Retrieve a single instance of the given model."""

        if isinstance('uuid', UUID):
            return db.session.get(model, kwargs.get('uuid'))

        query = db.session.execute(db.select(model).filter_by(**kwargs))

        return query.scalar_one_or_none() if not fetch_all else query.scalars().all()

    def update(self, model: type[db.Model], uuid: UUID, **kwargs) -> db.Model:
        """Update and return the instance of the given model with the specified UUID."""

        instance = self.retrieve(model, uuid=uuid)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            db.session.commit()
        return instance

    def delete(self, model: type[db.Model], uuid: UUID) -> db.Model:
        """Delete and return the instance of the given model with the specified UUID."""

        instance = self.retrieve(model, uuid=uuid)
        if instance:
            db.session.delete(instance)
            db.session.commit()
        return instance


sqlalchemy_client = SQLAlchemyClient()
