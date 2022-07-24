import os

from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from app.admin import admin_blueprint
from app.auth import auth_blueprint, user_blueprint
from app.database import database
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.doctor import doctor_blueprint
from config import DevelopmentConfig

# configure installed apps
app = Flask(__name__)
migrate = Migrate(app, database)
jwt = JWTManager(app)
CORS(app)
load_dotenv()
database.init_app(app)

# APP CONFIGS
app.secret_key = os.getenv('SECRET_KEY')
app.config.from_object(DevelopmentConfig)

#Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(doctor_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    # open_json = open('static/dummy_data/patients11.json')
    # data = json.load(open_json)
    #
    # provider = ProviderTable.query.all()[randrange(3000)]
    # registration = RegistrationTable.query.all()[randrange(1)]
    # unit = UnitTable.query.all()[randrange(21)]
    # service_area = ServiceAreaTable.query.all()[randrange(7)]
    #
    #
    # for patient in data:
    #     new_patient = PatientTable(
    #         title=patient['title'],
    #         first_name=patient['first_name'],
    #         middle_name=patient['middle_name'] if patient['middle_name'] else '',
    #         last_name=patient['last_name'],
    #         username=patient['username'],
    #         email=patient['email'],
    #         password=generate_password_hash('password'),
    #         gender=patient['gender'],
    #         date_of_birth=patient['date_of_birth'],
    #         phone_number=patient['phone_number'],
    #         profile_image_url=os.getenv('DEFAULT_PROFILE_IMG'),
    #         patient_hospital_id=patient['patient_hospital_id'],
    #         consultant_id='3b557778-c48c-4630-9774-769eb349509b',
    #         religion='Islam',
    #         occupation=patient['occupation'],
    #         relationship_status='In A Relationship',
    #         next_of_kin_name=patient['next_of_kin_name'],
    #         next_of_kin_phone=patient['next_of_kin_phone'],
    #         next_of_kin_address=patient['next_of_kin_address'],
    #         next_of_kin_gender=patient['next_of_kin_gender'],
    #         next_of_kin_relationship='Brother',
    #         registration_id=registration.id,
    #         unit_id=unit.id,
    #         service_area_id=service_area.id,
    #     )
    #     address = register_address(address=patient, patient_id=new_patient.id)
    #     new_patient.address_id = address.id
    #     new_patient.save_to_db()
    #     print(f"Added {new_patient.title} {new_patient.first_name} {new_patient.last_name}")
    # success_response = make_response('Patients Successfully Created')
    # success_response.status_code = 201
    # return success_response
    return str(os.getenv('MAIL_USERNAME'))


@app.before_first_request
def create_tables():
    database.create_all()


if __name__ == '__main__':
    database.init_app(app)
    app.run(port=5000, debug=True)
