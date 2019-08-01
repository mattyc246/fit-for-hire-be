from flask import Blueprint, request, jsonify, make_response
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

sessions_api_blueprint = Blueprint(
    'sessions_api', __name__, template_folder='templates')


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

    access_token = create_access_token(identity=user.id)

    response = {
        'message': 'Logged in successfully',
        'valid': True,
        'auth_token': access_token
    }

    return make_response(jsonify(response), 200)
