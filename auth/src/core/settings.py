from logging import config as logging_config
from pathlib import Path

from pydantic import BaseSettings, PostgresDsn, RedisDsn

from .logger import LOGGING_CONFIG

logging_config.dictConfig(LOGGING_CONFIG)

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    """Settings class to read environment variables."""

    project_name: str
    postgres_dsn: PostgresDsn
    redis_dsn: RedisDsn
    jwt_secret_key: str
    access_token_expires: int
    refresh_token_expires: int

    class Config:
        env_file = BASE_DIR / '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
