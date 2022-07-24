import os
from flask import make_response
from werkzeug.security import generate_password_hash

from app import ProviderTable
from app.utils import register_address


def create_provider(provider):
    new_provider_object = ProviderTable(
        title=provider['title'],
        first_name=provider['first_name'],
        middle_name=provider['middle_name'],
        last_name=provider['last_name'],
        date_of_birth=provider['date_of_birth'],
        username=provider['username'],
        email=provider['email'],
        password=generate_password_hash(provider['password']),
        gender=provider['gender'],
        phone_number=provider['phone_number'],
        profile_image_url=os.getenv('DEFAULT_PROFILE_IMG'),
        staff_id=provider['staff_id'],
        is_consultant=provider['is_consultant'],
        specialty=provider['specialty'],
        department_id=provider['department_id'],
        unit_id=provider['unit_id'],
        service_area_id=provider['service_area_id'],
        role_id=provider['role_id']
    )
    address = register_address(address=provider, provider_id=new_provider_object.id)
    new_provider_object.address_id = address.id
    new_provider_object.save_to_db()
    success_response = make_response('New Provider Successfully Created')
    success_response.status_code = 201
    return success_response
