from pathlib import Path

from pydantic import BaseSettings, Field, PostgresDsn, RedisDsn

BASE_DIR = Path(__file__).resolve().parents[1]


class TestSettings(BaseSettings):
    """Settings class to read environment variables."""

    postgres_dsn: PostgresDsn = Field(default='postgresql://test:123qwe@localhost:5432/web')
    redis_dsn: RedisDsn = Field(default='redis://web:123qwe@localhost:6379/2')


test_settings = TestSettings()
