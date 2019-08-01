from flask import Blueprint, request, make_response, jsonify
from models.user import User
from werkzeug.security import generate_password_hash

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


@users_api_blueprint.route('/', methods=['POST'])
def create():
    full_name = request.form.get('full_name')
    username = request.form.get('username')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    date_of_birth = request.form.get('date_of_birth')
    password = request.form.get('password')

    hashed_password = generate_password_hash(password)

    user = User(
        full_name=full_name,
        username=username,
        email=email,
        phone_number=phone_number,
        date_of_birth=date_of_birth,
        password=hashed_password
    )

    if user.save():
        response = {
            'message': 'Successfully created account with Fit4Hire',
            'created': True
        }

        return make_response(jsonify(response), 200)

    response = {
        'message': 'Failed to create account',
        'created': False
    }

    return make_response(jsonify(response), 400)
