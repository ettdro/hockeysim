from hockeysim import create_app
#from hockeysim.config import TestConfig
#from hockeysim.models.division import Division
from hockeysim.database import migrate, db
import pytest
#import flask


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""

    app = create_app(True)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


'''@pytest.fixture
def mock_division():
    division = Division('Atlantic', 'ATL')
    return division


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch(
        "flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


@pytest.fixture
def mock_division_id(mocker):
    mock = mocker.patch(
        "hockeysim.models.division.Division.id", new_callable=mocker.PropertyMock, return_value=32193221)
    return mock'''
