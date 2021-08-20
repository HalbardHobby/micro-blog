import os
from flask import Flask

from . import posts

def create_app():
    app = Flask(__name__)
    app.register_blueprint(posts.bp)
    return app
