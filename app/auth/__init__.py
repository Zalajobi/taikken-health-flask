import os
from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, url_prefix=f"{os.getenv('BASE_URL')}auth")
user_blueprint = Blueprint('user', __name__, url_prefix=f"{os.getenv('BASE_URL')}user")

from . import views
