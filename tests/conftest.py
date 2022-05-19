from typing import Generator
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from microblog import create_app
from flask_wtf.csrf import CSRFProtect
from microblog.config import TestConfig
import pytest


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    """Get the flask app with test configurations

    Yields:
        Generator[Flask, None, None]: Flask app
    """
    app = create_app(TestConfig)
    CSRFProtect(app)
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """creates a test client for the application

    Args:
        app (Flask): The app Flask object

    Returns:
        FlaskClient: A flask test client that works like the app but for testing
    """
    with app.test_client() as client:
        with app.app_context():
            yield client



@pytest.fixture
def runner(app:Flask) -> FlaskCliRunner:
    """creates a runner that can call the Click commands registered with the application

    Args:
        app (Flask): The app Flask object

    Returns:
        FlaskCliRunner: an instance of test_cli_runner_class
    """
    return app.test_cli_runner()
