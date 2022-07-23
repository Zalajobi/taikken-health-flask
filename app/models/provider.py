import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel, BaseUserModel


class ProviderTable(BaseModel, BaseUserModel, database.Model):
    """Table responsible for interacting with the providers' table in the database"""
    __tablename__ = 'provider'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    department_id = database.Column(UUID(as_uuid=True), database.ForeignKey('department.id'))
    unit_id = database.Column(UUID(as_uuid=True), database.ForeignKey('unit.id'))
    service_area_id = database.Column(UUID(as_uuid=True), database.ForeignKey('service_area.id'))
    role_id = database.Column(UUID(as_uuid=True), database.ForeignKey('role.id'))
    address_id = database.Column(UUID(as_uuid=True), database.ForeignKey('address.id'))
    staff_id = database.Column(database.String(30), nullable=False, unique=True, index=True)
    is_consultant = database.Column(database.Boolean(), nullable=False, default=False)
    specialty = database.Column(database.String(100))

    # Database relationships
    inbox = database.relationship('InboxTable', backref='provider', lazy=True, cascade="all,delete")
    patient = database.relationship('PatientTable', backref='provider', lazy=True)

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

    def __repr__(self):
        return '<ProviderTable {}>'.format(self.username)
