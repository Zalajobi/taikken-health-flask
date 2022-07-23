from app.database import database
from datetime import datetime
from sqlalchemy import func


class BaseModel:
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)

    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    time_updated = database.Column(database.DateTime, nullable=False, default=datetime.utcnow, onupdate=func.now())
