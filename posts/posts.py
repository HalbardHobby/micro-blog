import uuid
import requests
from flask import Blueprint, request, jsonify

bp = Blueprint('posts', __name__, url_prefix='/posts')

post_list = []

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def list_posts():
    return jsonify(post_list), 200

@bp.route('/', methods=['POST'])
def create_post():
    req = request.get_json()
    new_post = { 'id': str(uuid.uuid4())[:8], 'title': req['title'] }
    post_list.append(new_post)

    requests.post(url='http://localhost:4999/events/', json={
        'type': 'PostCreated',
        'data': new_post
    })

    return jsonify(new_post), 201
