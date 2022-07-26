import os
from flask import make_response
from werkzeug.security import generate_password_hash

from app import ProviderTable, PatientTable
from app.utils import register_address


def create_provider(provider):
    new_provider_object = ProviderTable(
        title=provider['title'],
        first_name=provider['first_name'],
        middle_name=provider['middle_name'] if provider['middle_name'] else '',
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


def register_new_patient(patient):
    new_patient = PatientTable(
        title=patient['title'],
        first_name=patient['first_name'],
        middle_name=patient['middle_name'] if patient['middle_name'] else '',
        last_name=patient['last_name'],
        username=patient['username'],
        email=patient['email'],
        password=generate_password_hash(patient['password']),
        gender=patient['gender'],
        date_of_birth=patient['date_of_birth'],
        phone_number=patient['phone_number'],
        profile_image_url=os.getenv('DEFAULT_PROFILE_IMG'),
        patient_hospital_id=patient['patient_hospital_id'],
        consultant_id=patient['consultant_id'],
        religion=patient['religion'],
        occupation=patient['occupation'],
        relationship_status=patient['relationship_status'],
        next_of_kin_name=patient['next_of_kin_name'],
        next_of_kin_phone=patient['next_of_kin_phone'],
        next_of_kin_address=patient['next_of_kin_address'],
        next_of_kin_gender=patient['next_of_kin_gender'],
        next_of_kin_relationship=patient['next_of_kin_relationship'],
        registration_id=patient['registration_id'],
        unit_id=patient['unit_id'],
        service_area_id=patient['service_area_id'],
    )
    address = register_address(address=patient, patient_id=new_patient.id)
    new_patient.address_id = address.id
    new_patient.save_to_db()
    success_response = make_response('New Patient Successfully Created')
    success_response.status_code = 201
    return success_response
