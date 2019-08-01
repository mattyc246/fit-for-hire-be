from flask import Blueprint, request, jsonify, make_response
from models.user import User
from werkzeug.security import check_password_hash

sessions_api_blueprint = Blueprint('sessions_api', __name__, template_folder='templates')

@sessions_api_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.get_or_none(User.username == username)

    if not user:
        response = {
            'message': 'No such user exists with the username provided',
            'valid': False
        }

        return make_response(jsonify(response), 401)

    if not check_password_hash(user.password, password):
        response = {
            'message': 'Incorrect password provided',
            'valid': False
        }

        return make_response(jsonify(response), 401)

    