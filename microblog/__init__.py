from flask import Flask
from .utils.db import microblog_db

def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import home
    app.register_blueprint(home.bp)

    app.db = microblog_db


    return app
