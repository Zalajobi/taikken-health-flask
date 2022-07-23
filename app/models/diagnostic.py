import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.database import database
from app.models.base import BaseModel


class DiagnosticTable(BaseModel):
    """Table responsible for interacting with the diagnostic table in the database"""
    __tablename__ = 'diagnostic'

    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    patient_id = database.Column(UUID(as_uuid=True), database.ForeignKey('patient.id'))
    summary = database.Column(database.Text(), nullable=False)
    medications = database.Column(database.String(), nullable=False)

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def __repr__(self):
        return '<DiagnosticTable {}>'.format(self.username)
