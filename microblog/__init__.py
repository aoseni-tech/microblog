from flask import Flask
from flask_wtf.csrf import CSRFProtect
from . import schema, config

csrf = CSRFProtect()


def create_app(app_config=config.DevConfig) -> Flask:
    """Application factory function

    Args:
        test_config (bool, optional): _description_. Defaults to False.

    Returns:
        Flask: The flask app object
    """
    app = Flask(__name__)

    app.config.from_object(app_config)

    app.entry_form = schema.EntryForm

    csrf.init_app(app)
    from .utils import db, app_errors

    db.init_db(app)
    app.register_error_handler(404, app_errors.handle_exception)

    from .routes import home

    app.register_blueprint(home.bp)

    return app
