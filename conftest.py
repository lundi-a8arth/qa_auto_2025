import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def github_api_unauthorised():
    api = GitHub()
    api.headers = {}
    yield api


@pytest.fixture
def db():
    database = Database()
    yield database
    database.connection.close()
