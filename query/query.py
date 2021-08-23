from flask import Blueprint, request, jsonify

bp = Blueprint('query', __name__, url_prefix=None)

@bp.route('/events/', methods=['POST'])
def receive_event():
    print( 'Event received: ', jsonify(request.get_json()) )
    return '', 200

@bp.route('/posts/', methods=['GET'])
def list_posts():
    return '', 200