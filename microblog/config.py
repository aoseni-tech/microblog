from dotenv import dotenv_values

config = dotenv_values(".env")


class Config:
    """Base config for flask app."""

    SECRET_KEY = config.get("SECRET_KEY")
    DATABASE = config.get("DATABASE")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    TESTING = False
    DEBUG = True
    MONGO_URI = config.get("MONGO_URI")


class ProdConfig(Config):
    """App config for production"""

    ENV = "production"


class DevConfig(Config):
    """App config for development"""

    ENV = "development"


class TestConfig:
    """App config for testing

    Args:
        Config (DevConfig): The development config class
    """

    ENV = "testing"
    DATABASE = config.get("TEST_DATABASE")
    MONGO_URI = config.get("TEST_MONGO_URI")
    SECRET_KEY = config.get("TEST_SECRET_KEY")
    TESTING = True


mode = config.get("MODE")

env_config = DevConfig
if mode == "PRODUCTION":
    env_config = ProdConfig
