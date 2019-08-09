from flask import Blueprint, request, make_response, jsonify
from models.user import User
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


@users_api_blueprint.route('/', methods=['GET'])
@jwt_required
def index():
    user_id = get_jwt_identity()

    user = User.get_or_none(User.id == user_id)

    if not user:
        response = {
            'message': 'No user identified'
        }

        return make_response(jsonify(response), 401)

    user_info = {
        'user_id': user.id,
        'full_name': user.full_name,
        'username': user.username
    }

    response = {
        'message': 'Successfully identified user',
        'user': user_info
    }

    return make_response(jsonify(response), 200)


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


@users_api_blueprint.route('/search', methods=['GET'])
@jwt_required
def search():
    query = request.args.get('q')

    users = User.select().where(
        ((User.full_name.contains(query))
         | (User.username.contains(query))
         | (User.profession.contains(query))) & (User.profession.not_in(['Customer'])
                                                 ))

    results = []

    for user in users:
        results.append({
            'id': user.id,
            'full_name': user.full_name,
            'username': user.username,
            'phone_number': user.phone_number,
            'profession': user.profession
        })

    response = {
        'users': results
    }

    return make_response(jsonify(response), 200)
