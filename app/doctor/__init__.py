import os
from flask import Blueprint

doctor_blueprint = Blueprint('doctor', __name__, url_prefix=f"{os.getenv('BASE_URL')}doctor")

from . import views
