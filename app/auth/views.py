import os
from app.auth import auth_blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


@auth_blueprint.route('/')
def hello_world():
    return str(os.getenv('DEFAULT_PROFILE_IMG'))


@auth_blueprint.route('/register/provider', methods=['POST'])
@jwt_required()
def provider_registration():
    id = get_jwt_identity()
    return 'password'


@auth_blueprint.route('/login/provider')
def login():
    return 'HELLO'
