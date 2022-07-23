import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel


class InboxTable(BaseModel, database.Model):
    """Table responsible for interacting with the inbox table in the database"""
    __tablename__ = 'inbox'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    # provider_recipient_id = database.Column(UUID(as_uuid=True), database.ForeignKey('provider.id'))
    patient_recipient_id = database.Column(UUID(as_uuid=True), database.ForeignKey('patient.id'))
    # service_area_id = database.Column(UUID(as_uuid=True), database.ForeignKey('service_area.id'))
    # role_id = database.Column(UUID(as_uuid=True), database.ForeignKey('role.id'))
    # unit_id = database.Column(UUID(as_uuid=True), database.ForeignKey('unit.id'))
    # department_id = database.Column(UUID(as_uuid=True), database.ForeignKey('department.id'))
    title = database.Column(database.String(100), nullable=False)
    message = database.Column(database.Text(), nullable=False)

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_all_by_provider_recipient_id(cls, provider_id):
        return cls.query.filter_by(provider_recipient_id=provider_id).all()

    @classmethod
    def find_all_by_patient_recipient_id(cls, patient_id):
        return cls.query.filter_by(patient_recipient_id=patient_id).all()

    @classmethod
    def find_all_by_department(cls, department_id):
        return cls.query.filter_by(department_id=department_id).all()

    @classmethod
    def find_all_by_unit(cls, unit_id):
        return cls.query.filter_by(unit_id=unit_id).all()

    @classmethod
    def find_all_by_department(cls, service_area_id):
        return cls.query.filter_by(service_area_id=service_area_id).all()

    @classmethod
    def find_all_by_department(cls, role_id):
        return cls.query.filter_by(role_id=role_id).all()

    def __repr__(self):
        return '<ID {}>'.format(self.id)