from flask import Blueprint, request, jsonify

bp = Blueprint('query', __name__, url_prefix=None)

posts = {}


@bp.route('/events/', methods=['POST'])
def receive_event():
    req = request.get_json()
    if req['type'] == 'PostCreated':
        posts[req['data']['id']] = {
            'id': req['data']['id'],
            'title': req['data']['title'],
            'comments': []
        }
    elif req['type'] == 'CommentCreated':
        comment = {
            'id': req['data']['id'],
            'content': req['data']['content'],
            'postId': req['data']['postId'],
            'status': req['data']['status']
        }
        posts[req['data']['postId']]['comments'].append(comment)

    return '', 201


@bp.route('/posts/', methods=['GET'])
def list_posts():
    return jsonify(posts), 200
