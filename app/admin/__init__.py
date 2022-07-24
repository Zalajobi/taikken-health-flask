import os
from flask import Blueprint

admin_blueprint = Blueprint('admin', __name__, url_prefix=f"{os.getenv('BASE_URL')}admin")

from . import views
