import pytest
import os

from dotenv import load_dotenv
from faker import Faker
from app import DepartmentTable
from app.database import database
from app.app import app
from config import TestingConfig

load_dotenv()


def test_db_create(app):
    app = app(TestingConfig)
    fake = Faker()

    department = DepartmentTable(
        name=fake.name(),
        description=fake.text()
    )
    department.save_to_db()

    assert database.session.query(DepartmentTable).one()
