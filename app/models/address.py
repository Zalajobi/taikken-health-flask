import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models import patient
from app.models.base import BaseModel


class AddressTable(BaseModel, database.Model):
    """Table responsible for interacting with the address table in the database"""
    __tablename__ = 'address'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    patient_id = database.Column(UUID(as_uuid=True), database.ForeignKey('patient.id'))
    provider_id = database.Column(UUID(as_uuid=True), database.ForeignKey('patient_id'))
    country = database.Column(database.String(60), nullable=False)
    address = database.Column(database.Text(), nullable=False)
    city = database.Column(database.String(60), nullable=False)
    zip_code = database.Column(database.Integer(), nullable=False)

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_provider_id(cls, provider_id):
        return cls.query.filter_by(provider_id=provider_id).first()

    @classmethod
    def find_by_patient_id(cls, patient_id):
        return cls.query.filter_by(patient_id=patient_id).first()

    def __repr__(self):
        return '<AddressTable {}>'.format(self.id)
