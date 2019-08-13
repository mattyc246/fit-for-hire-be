from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.message import Message
from models.chat_room import ChatRoom

messages_api_blueprint = Blueprint(
    'messages_api', __name__, template_folder='templates')


@messages_api_blueprint.route('/all', methods=['GET'])
@jwt_required
def all():
    room_no = request.args.get('room_no')
    room = ChatRoom.get(ChatRoom.room_no == room_no)

    messages = Message.select().where(Message.room_id == room.id)

    out_messages = []

    for message in messages:
        out_messages.append({
            'body': message.body,
            'username': message.sender.username
        })

    response = {
        'messages': out_messages
    }

    return make_response(jsonify(response), 200)
