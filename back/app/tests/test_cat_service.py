import os
import pytest
from app.services.cat_service import CatService
from app.models import Cat, Vaccination
from pymongo import MongoClient
from datetime import date, datetime
from dotenv import load_dotenv

from app.services.config_service import ConfigService

# Load environment variables from .env file
load_dotenv()

@pytest.fixture
def cat_service():
    config_service = ConfigService()
    service = CatService(config_service)
    dbname = config_service.get('MONGODB_DATABASE_NAME')
    yield service
    service.client[dbname].cats.delete_many({})

def test_create_cat(cat_service):
    cat = Cat(name="Mittens", image="base64EncodedImage", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    assert cat_id is not None

def test_read_cat(cat_service):
    cat = Cat(name="Mittowns", image="base64EncodedImage", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    fetched_cat = cat_service.get_cat(cat_id)
    assert fetched_cat['name'] == "Mittowns"
    assert fetched_cat['id'] == cat_id

def test_update_cat(cat_service):
    cat = Cat(name="Mittens", image="base64EncodedImage", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    updated_cat = Cat(name="Whiskers",image="base64EncodedImage", age=5, breed="Sphynx", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    success = cat_service.update_cat(cat_id, updated_cat)
    assert success

def test_delete_cat(cat_service):
    cat = Cat(name="Mittens", image="base64EncodedImage", age=3, breed="Siamese", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_id = cat_service.create_cat(cat)
    success = cat_service.delete_cat(cat_id)
    assert success

def test_list_cats(cat_service):
    cat = Cat(name="Pickles", image="base64EncodedImage", age=3, breed="Normal", vaccinations=[Vaccination(type="Flu", date=datetime.today())])
    cat2 = Cat(name="Friskies", image="base64EncodedImage", age=5, breed="Magical", vaccinations=[Vaccination(type="Rabies", date=datetime.today())])
    cat_service.create_cat(cat)
    cat_service.create_cat(cat2)
    cats = cat_service.list_cats()
    assert len(cats) == 2
    assert cats[0]['name'] == "Pickles"
    assert cats[1]['name'] == "Friskies"
    assert cats[0]['breed'] == "Normal"
    assert cats[1]['breed'] == "Magical"
    assert cats[0]['vaccinations'][0]['type'] == "Flu"
    assert cats[1]['vaccinations'][0]['type'] == "Rabies"
    assert cats[0]['id'] is not None