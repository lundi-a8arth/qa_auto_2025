import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.login_page import LoginPage
from modules.ui.page_objects.exceptions_page import ExceptionsPage


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


@pytest.fixture
def login_page():
    login_page = LoginPage()
    yield login_page
    login_page.quit()


@pytest.fixture
def exceptions_page():
    exceptions_page = ExceptionsPage()
    yield exceptions_page
    exceptions_page.quit()
