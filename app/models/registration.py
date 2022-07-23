import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel


class RegistrationTable(BaseModel):
    """Table responsible for interacting with the patients' table in the database"""
    __tablename__ = 'registration'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = database.Column(database.String(), nullable=False)
    description = database.Column(database.Text(), nullable=False)

    # Database Relation(s)
    patient = database.relationship('PatientTable', backref='relationship', lazy=True, cascade="save-update")

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '<RegistrationTable {}>'.format(self.username)
