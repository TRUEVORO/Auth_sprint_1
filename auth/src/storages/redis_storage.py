from clients import RedisClient

from .base_storage import BaseStorage


class RedisStorage(BaseStorage):
    """Redis storage."""

    def __init__(self, redis: RedisClient) -> None:
        """Initialize async Redis storage."""

        self.redis: RedisClient = redis

    def save_data(self, key: str, value: str, ttl: int | None = None) -> None:
        """Save data in Redis."""

        self.redis.create(name=key, value=value, ex=ttl)

    def retrieve_data(self, key: str) -> str | bytes | None:
        """Retrieve data from Redis."""

        return self.redis.retrieve(key)
