from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

chats_api_blueprint = Blueprint(
    'chats_api', __name__, template_folder='templates')


@chats_api_blueprint.route('/', methods=['POST'])
def create():
    pass


@chats_api_blueprint.route('/active_chats', methods=['GET'])
@jwt_required
def active_chats():
    user_id = get_jwt_identity()

    response = {
        'chats': []
    }

    return make_response(jsonify(response), 200)
