from flask import Blueprint, request, jsonify

bp = Blueprint('query', __name__, url_prefix=None)

posts = {}


def handle_event(req):
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

    elif req['type'] == 'CommentUpdated':
        comments = posts[req['data']['postId']]['comments']
        id = req['data']['id']
        comm = next((x for x in comments if x['id'] == id), None)

        comm['content'] = req['data']['content']
        comm['status'] = req['data']['status']


@bp.route('/events/', methods=['POST'])
def receive_event():
    req = request.get_json()
    handle_event(req)

    return '', 201


@bp.route('/posts/', methods=['GET'])
def list_posts():
    return jsonify(posts), 200
