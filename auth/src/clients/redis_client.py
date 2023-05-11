from pydantic import RedisDsn
from redis import Redis
from redis.typing import EncodableT, KeyT

from .base_client import BaseClient


class RedisClient(BaseClient):
    """Client for Redis providing CRUD operations on database models."""

    def __init__(self, dsn: RedisDsn, connection: Redis | None = None):
        """Initialization of redis client."""

        self.dsn: RedisDsn = dsn
        self._connection: Redis | None = connection

    def _reconnect(self) -> Redis:
        """Reconnect to Redis if no connection exists."""

        return Redis(host=self.dsn.host, port=int(self.dsn.port), db=self.dsn.path[1:])

    @property
    def connection(self) -> Redis:
        """Redis client connection."""

        return self._connection if self._connection else self._reconnect()

    def create(self, name: KeyT, value: EncodableT, ex: float | None = None, **kwargs) -> None:
        """Create and return a new instance of the given model."""

        self.connection.set(name=name, value=value, ex=ex)

    def retrieve(self, name: KeyT) -> bytes | None:
        """Retrieve a single instance of the given model."""

        return self.connection.get(name)

    def update(self, *args, **kwargs) -> None:
        """Update and return the instance of the given model with the specified UUID."""

        raise NotImplementedError

    def delete(self, *names) -> None:
        """Delete and return the instance of the given model with the specified UUID."""

        self.connection.delete(names)
