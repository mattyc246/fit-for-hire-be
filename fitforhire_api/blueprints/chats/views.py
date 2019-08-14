from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.chat_room import ChatRoom

chats_api_blueprint = Blueprint(
    'chats_api', __name__, template_folder='templates')


@chats_api_blueprint.route('/', methods=['POST'])
@jwt_required
def create():
    user_id = get_jwt_identity()
    professional_id = request.json['p_id']

    room_no = f"{user_id}-{professional_id}"

    chatroom_exists = ChatRoom.get_or_none(ChatRoom.room_no == room_no)

    if not chatroom_exists:

        customer = User.get_by_id(user_id)
        professional = User.get_by_id(professional_id)

        chat_room = ChatRoom(
            customer=customer,
            professional=professional,
            room_no=f"{customer.id}-{professional_id}"
        )

        if chat_room.save():
            response = {
                'ok': True,
                'message': 'Room Created',
                'professional': {
                    'username': professional.username
                }
            }

            return make_response(jsonify(response), 200)

        response = {
            'ok': False,
            'message': 'Unable to create room'
        }

        return make_response(jsonify(response), 400)

    response = {
        'ok': True,
        'message': 'Chat exists',
        'professional': {
            'username': professional.username
        }
    }

    return make_response(jsonify(response), 200)


@chats_api_blueprint.route('/active_chats', methods=['GET'])
@jwt_required
def active_chats():
    user_id = get_jwt_identity()

    chat_rooms = ChatRoom.select().where(ChatRoom.customer_id == user_id)

    chats = []

    for chat in chat_rooms:
        chats.append({
            'room_no': chat.room_no,
            'professional': {
                'id': chat.professional_id,
                'username': chat.professional.username
            }
        })

    response = {
        'chats': chats
    }

    return make_response(jsonify(response), 200)


@chats_api_blueprint.route('/last_four', methods=['GET'])
@jwt_required
def last_four():
    user_id = get_jwt_identity()

    chat_rooms = ChatRoom.select().where(ChatRoom.customer_id == user_id).order_by(
        ChatRoom.created_at.desc()).limit(4)

    chats = []

    for chat in chat_rooms:
        chats.append({
            'room_no': chat.room_no,
            'professional': {
                'id': chat.professional_id,
                'username': chat.professional.username
            }
        })

    response = {
        'chats': chats
    }

    return make_response(jsonify(response), 200)
