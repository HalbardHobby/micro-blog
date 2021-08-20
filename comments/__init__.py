import os
from flask import Flask
from flask_cors import CORS

from . import comments

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(comments.bp)
    return app
