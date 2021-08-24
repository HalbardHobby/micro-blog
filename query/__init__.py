import os
from flask import Flask, jsonify
import requests
from flask_cors import CORS

from . import query


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(query.bp)

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    res = requests.get(url='http://localhost:4999/events/').json()
    map(query.handle_event, res)

    return app
