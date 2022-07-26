import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel


class AllergyTable(BaseModel, database.Model):
    """Table responsible for interacting with the allergy table in the database"""
    __tablename__ = 'allergy'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    patient_id = database.Column(UUID(as_uuid=True), database.ForeignKey('patient.id'))
    name = database.Column(database.String(), nullable=False)
    description = database.Column(database.Text(), nullable=False)

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '<AllergyTable {}>'.format(self.id)
