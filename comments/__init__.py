import os
from flask import Flask

from . import comments

def create_app():
    app = Flask(__name__)
    app.register_blueprint(comments.bp)
    return app
