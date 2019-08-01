from fitforhire_api.blueprints.users.views import users_api_blueprint
from fitforhire_api.blueprints.sessions.views import sessions_api_blueprint
from app import app
from flask_cors import CORS
from flask_jwt_extended import JWTManager

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##


app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/sessions')
jwt = JWTManager(app)
