import os
from flask import Flask, jsonify
from flask_cors import CORS

from . import comments

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(comments.bp)

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    return app
