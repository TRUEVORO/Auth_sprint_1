from clients import RedisClient
from core import settings
from storages import RedisStorage

redis_storage: RedisStorage = RedisStorage(RedisClient(dsn=settings.redis_dsn))
