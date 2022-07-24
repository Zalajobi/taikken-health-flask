import os
import json
from datetime import datetime, timedelta
from random import randrange

from flask import request, make_response

from app import ProviderTable, database, RoleTable, ServiceAreaTable, DepartmentTable, UnitTable
from app.auth import auth_blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash


@auth_blueprint.route('/')
def hello_world():
    return str(os.getenv('DEFAULT_PROFILE_IMG'))


# @auth_blueprint.route('/register/provider', methods=['GET'])
# # @jwt_required()
# def provider_registration():
#     # id = get_jwt_identity()
#
#     json_file = open('static/dummy_data/providers3.json')
#     data = json.load(json_file)
#     for provider in data:
#         role = RoleTable.query.all()[randrange(12)]
#         service_area = ServiceAreaTable.query.all()[randrange(7)]
#         department = DepartmentTable.query.all()[randrange(41)]
#         unit = UnitTable.query.all()[randrange(22)]
#
#         new_provider = ProviderTable(
#             title=provider['title'],
#             first_name=provider['first_name'],
#             middle_name=provider['middle_name'],
#             last_name=provider['last_name'],
#             date_of_birth=provider['date_of_birth'],
#             username=provider['username'],
#             email=provider['email'],
#             password=generate_password_hash('password'),
#             gender=provider['gender'],
#             phone_number=provider['phone_number'],
#             profile_image_url=os.getenv('DEFAULT_PROFILE_IMG'),
#             staff_id=provider['staff_id'],
#             is_consultant=provider['is_consultant'],
#             specialty=provider['specialty'],
#             department_id=department.id,
#             unit_id=unit.id,
#             service_area_id=service_area.id,
#             role_id=role.id
#         )
#         new_provider.save_to_db()
#         print(f"Saved {new_provider.username} to DB")
#     return 'password'


@auth_blueprint.route('/login/provider', methods=['POST'])
def login():
    content = request.json
    error_response = make_response('Invalid Username or Password')
    error_response.status_code = 401

    try:
        provider = ProviderTable.find_by_username(content['username']) or \
                   ProviderTable.find_by_email(content['username'])
        if provider is None:
            return error_response
        elif check_password_hash(provider.password, content['password']):
            # additional_jwt_data = {"active_role_id": role.id, "active_role_name": role.name}
            # success_response = make_response({"token": create_access_token(
            #     identity=provider.id, expires_delta=datetime.timedelta(hours=6, minutes=30),
            #     additional_claims=additional_jwt_data)})
            success_response = make_response({"token": create_access_token(
                identity=provider.id, expires_delta=timedelta(hours=6, minutes=30))})
            success_response.status_code = 200
            return success_response
    except Exception as e:
        return error_response
