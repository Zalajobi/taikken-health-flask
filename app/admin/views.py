from flask import request, make_response

from app.admin import admin_blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from .utils import *
from ..utils import get_provider


@admin_blueprint.route('/register/provider', methods=['POST'])
@jwt_required()
def admin_create_provider():
    content = request.json
    provider = get_provider(get_jwt_identity())

    try:
        if provider.role.name != 'admin':
            error_response = make_response('Current user is unauthorized to register new staff')
            error_response.status_code = 401
            return error_response
        else:
            return create_provider(content)
    except Exception as e:
        error_response = make_response('Provider Missing Required Information')
        error_response.status_code = 400
        return error_response
