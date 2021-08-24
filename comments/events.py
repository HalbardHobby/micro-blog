from flask import Blueprint, request, jsonify
import requests
from . import comments

bp = Blueprint('events', __name__, url_prefix='/events')


@bp.route('/', methods=['POST'])
def receive_event():
    req = request.get_json()

    if req['type'] == 'CommmentModerated':
        id = req['data']['id']
        postId = req['data']['postId']
        status = req['data']['status']

        comms = comments.comments_by_post[postId]
        comment = next((x for x in comms if x['id'] == id), None)
        comment['status'] = status

        requests.post(url='http://localhost:4999/events/', json={
        'type': 'CommentUpdated',
        'data': {
            'id': id,
            'content': comment['content'],
            'postId': postId,
            'status': status,
        }
    })

    # print( 'Event received: ', jsonify(request.get_json()) )
    return '', 200
