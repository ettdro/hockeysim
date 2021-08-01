import tempfile

class DevConfig:
    TESTING=False
    SECRET_KEY='dev'
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:example@database:5432/hockeysim"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestConfig:
    TESTING=True
    SECRET_KEY='testing'
    SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS=False