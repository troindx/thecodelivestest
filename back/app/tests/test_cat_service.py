import os
import pytest
from app.services.cat_service import CatService
from app.models import Cat, Vaccination
from pymongo import MongoClient
from datetime import date, datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@pytest.fixture
def cat_service():
    MONGODB_PORT = os.getenv("MONGODB_PORT")
    MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME")
    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")

    MONGODB_URL = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DATABASE_NAME}"
    client = MongoClient(MONGODB_URL)
    service = CatService(db_url=MONGODB_URL, db_name=MONGODB_DATABASE_NAME)
    yield service
    client[MONGODB_DATABASE_NAME].cats.delete_many({})

def test_create_cat(cat_service):
    cat = Cat(name="Mittens", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    assert cat_id is not None

def test_read_cat(cat_service):
    cat = Cat(name="Mittowns", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    fetched_cat = cat_service.get_cat(cat_id)
    assert fetched_cat['name'] == "Mittowns"

def test_update_cat(cat_service):
    cat = Cat(name="Mittens", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    updated_cat = Cat(name="Whiskers", age=5, breed="Sphynx", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    success = cat_service.update_cat(cat_id, updated_cat)
    assert success

def test_delete_cat(cat_service):
    cat = Cat(name="Mittens", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    success = cat_service.delete_cat(cat_id)
    assert success

def test_list_cats(cat_service):
    cat = Cat(name="Pickles", age=3, breed="Normal", vaccinations=[Vaccination(type="Flu", date=datetime.today())])
    cat2 = Cat(name="Friskies", age=5, breed="Magical", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_service.create_cat(cat)
    cat_service.create_cat(cat2)
    cats = cat_service.list_cats()
    assert len(cats) == 2