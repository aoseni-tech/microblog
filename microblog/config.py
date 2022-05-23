from os import path, environ
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))


class Config:
    """Base config for flask app."""

    SECRET_KEY = environ.get("SECRET_KEY")
    DATABASE = environ.get("DATABASE")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    TESTING = False
    DEBUG = False
    MONGO_URI = environ.get("MONGO_URI")


class ProdConfig(Config):
    """App config for production"""

    ENV = "production"


class DevConfig(Config):
    """App config for development"""

    ENV = "development"
    DEBUG = True

class TestConfig:
    """App config for testing

    Args:
        Config (DevConfig): The development config class
    """

    ENV = "testing"
    DATABASE = environ.get("TEST_DATABASE")
    MONGO_URI = environ.get("TEST_MONGO_URI")
    SECRET_KEY = environ.get("TEST_SECRET_KEY")
    TESTING = True
    DEBUG = True

mode = environ.get("MODE")

env_config = DevConfig
if mode == "PRODUCTION":
    env_config = ProdConfig
