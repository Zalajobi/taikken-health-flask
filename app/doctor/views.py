from app import PatientTable
from app.doctor import doctor_blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required


@doctor_blueprint.route('/consultant/patients')
@jwt_required()
def doctors_primary_patient():
    primary_patients = PatientTable.find_all_by_consultant(get_jwt_identity())
    for patient in primary_patients:
        print(f"Patient {patient.title} {patient.first_name} {patient.last_name}")
    return "HELLO"
