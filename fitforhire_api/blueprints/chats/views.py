from flask import Blueprint

chats_api_blueprint = Blueprint(
    'chats_api', __name__, template_folder='templates')


@chats_api_blueprint.route('/', methods=['POST'])
def create():
    pass
