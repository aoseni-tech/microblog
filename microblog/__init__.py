from flask import Flask
from flask_wtf.csrf import CSRFProtect
from . import schema
from .config import env_config

csrf = CSRFProtect()


def create_app(app_config=env_config) -> Flask:
    """Application factory function

    Args:
        app_config : The app configuration variables

    Returns:
        Flask: The flask app object
    """
    app = Flask(__name__, static_folder="static")

    app.config.from_object(app_config)

    app.entry_form = schema.EntryForm

    csrf.init_app(app)

    from .utils import db, app_errors

    db.init_db(app)
    app.register_error_handler(404, app_errors.handle_exception)

    from .routes import home

    app.register_blueprint(home.bp)

    return app
