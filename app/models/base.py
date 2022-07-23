import os
from app.database import database
from datetime import datetime
from sqlalchemy import func


class BaseModel:
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)

    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    time_updated = database.Column(database.DateTime, nullable=False, default=datetime.utcnow, onupdate=func.now())


class BaseUserModel:
    def __init__(self, *args, **kwargs):
        super(BaseUserModel, self).__init__(*args, **kwargs)

    title = database.Column(database.String(30), nullable=False)
    first_name = database.Column(database.String(60), nullable=False)
    middle_name = database.Column(database.String(60))
    last_name = database.Column(database.String(60), nullable=False)
    username = database.Column(database.String(100), nullable=False, unique=True)
    email = database.Column(database.String(100), nullable=False, unique=True)
    password = database.Column(database.String(), nullable=False)
    gender = database.Column(database.String(30), nullable=False)
    date_of_birth = database.Column(database.Date(), nullable=False)
    phone_number = database.Column(database.Integer(), nullable=False, unique=True)
    profile_image_url = database.Column(database.String(), nullable=False, default=os.getenv('DEFAULT_PROFILE_IMG'))