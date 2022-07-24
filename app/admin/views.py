from flask import request

from app.admin import admin_blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from .utils import *
from ..utils import get_provider, generate_error_response


@admin_blueprint.route('/register/provider', methods=['POST'])
@jwt_required()
def admin_create_provider():
    content = request.json
    provider = get_provider(get_jwt_identity())

    try:
        if provider.role.name != 'admin':
            return generate_error_response(f'{provider.role.name} are not authorized to register new staff', 401)
        else:
            return create_provider(content)
    except Exception as e:
        return generate_error_response('Missing required fields. Check information', 400)


# admin or record officer can add patient
@admin_blueprint.route('/register/patient/', methods=['POST'])
@jwt_required()
def admin_create_patient():
    context = request.json
    provider = get_provider(get_jwt_identity())

    try:
        if provider.role.name == 'admin' or provider.role.name == 'record officer':
            return register_new_patient(context)
        else:
            return generate_error_response(f'{provider.role.name} are not authorized to register new patient', 401)

    except Exception as e:
        return generate_error_response('Missing required fields. Check provided information', 400)
