from hockeysim import create_app
from hockeysim.models import db
import pytest

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app(True)

    db.init_app(app)

    # create the database and load test data
    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
