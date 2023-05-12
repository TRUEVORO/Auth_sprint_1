import pytest
from flask_migrate import downgrade, upgrade

from src.app import create_app
from tests.settings import BASE_DIR, test_settings


@pytest.fixture(scope='session')
def client():
    app = create_app(test_settings.postgres_dsn, testing=True)
    with app.app_context():
        upgrade(directory=BASE_DIR / 'src/migrations')
        yield app.test_client()
        downgrade(directory=BASE_DIR / 'src/migrations')
