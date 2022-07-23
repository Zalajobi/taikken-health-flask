import os
from app.auth import auth_blueprint


@auth_blueprint.route('/')
def hello_world():
    return str(os.getenv('DEFAULT_PROFILE_IMG'))


@auth_blueprint.route('/signup')
def user_registration():
    return 'password'
