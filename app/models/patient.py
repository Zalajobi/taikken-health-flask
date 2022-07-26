import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel, BaseUserModel


class PatientTable(BaseModel, BaseUserModel, database.Model):
    """Table responsible for interacting with the patients' table in the database"""
    __tablename__ = 'patient'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    consultant_id = database.Column(UUID(as_uuid=True), database.ForeignKey('provider.id'))
    registration_id = database.Column(UUID(as_uuid=True), database.ForeignKey('registration.id'))
    unit_id = database.Column(UUID(as_uuid=True), database.ForeignKey('unit.id'))
    service_area_id = database.Column(UUID(as_uuid=True), database.ForeignKey('service_area.id'))
    address_id = database.Column(UUID(as_uuid=True), database.ForeignKey('address.id'))
    patient_hospital_id = database.Column(database.String(30), nullable=False, unique=True, index=True)
    religion = database.Column(database.String(60), nullable=False)
    occupation = database.Column(database.String(255), nullable=False)
    relationship_status = database.Column(database.String(100), nullable=False)
    next_of_kin_name = database.Column(database.String(255), nullable=False)
    next_of_kin_address = database.Column(database.String(255), nullable=False)
    next_of_kin_phone = database.Column(database.Integer(), nullable=False)
    next_of_kin_gender = database.Column(database.String(30), nullable=False)
    next_of_kin_relationship = database.Column(database.String(30), nullable=False)
    #
    # # Database relationships
    inbox = database.relationship('InboxTable', backref='patient', lazy=True, cascade="all,delete")
    diagnostic = database.relationship('DiagnosticTable', backref='patient', lazy=True, cascade="all,delete")
    allergy = database.relationship('AllergyTable', backref='patient', lazy=True, cascade="all,delete")

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all_by_consultant(cls, consultant_id):
        return cls.query.filter_by(consultant_id=consultant_id).all()

    def __repr__(self):
        return '<PatientTable {}>'.format(self.username)
