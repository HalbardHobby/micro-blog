from flask import Blueprint, request, jsonify

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/', methods=['POST'])
def receive_event():
    print( 'Event received: ', jsonify(request.get_json()) )
    return '', 200
