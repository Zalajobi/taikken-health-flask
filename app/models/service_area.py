import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel


class ServiceAreaTable(BaseModel, database.Model):
    """Table responsible for interacting with the service_area table in the database"""
    __tablename__ = 'service_area'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = database.Column(database.String(), nullable=False)
    description = database.Column(database.Text(), nullable=False)

    # Database Relationship
    inbox = database.relationship('InboxTable', backref='service_area', lazy=True, cascade="save-update")
    provider = database.relationship('ProviderTable', backref='service_area', lazy=True, cascade="all,delete")
    patient = database.relationship('PatientTable', backref='service_area', lazy=True, cascade="all,delete")

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '<ServiceAreaTable {}>'.format(self.name)
