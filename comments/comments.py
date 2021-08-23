import uuid
import requests
from flask import Blueprint, request, jsonify

bp = Blueprint('posts', __name__, url_prefix='/posts')

comments_by_post = {}


@bp.route('/<post_id>', methods=['GET'])
def list_comments(post_id):
    if post_id in comments_by_post:
        return jsonify(comments_by_post[post_id]), 200
    else:
        return jsonify([]), 200


@bp.route('/<post_id>', methods=['POST'])
def create_comment(post_id):
    req = request.get_json()
    new_comment = {'id': str(uuid.uuid4())[:8],
                   'content': req['content'],
                   'status': 'pending'
                   }

    if post_id not in comments_by_post:
        comments_by_post[post_id] = []

    comments_by_post[post_id].append(new_comment)

    requests.post(url='http://localhost:4999/events', json={
        'type': 'CommentCreated',
        'data': {
            'id': new_comment['id'],
            'content': new_comment['content'],
            'postId': post_id,
            'status': 'pending'
        }
    })

    return jsonify(new_comment), 201
