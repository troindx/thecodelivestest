from pymongo import MongoClient
from bson.objectid import ObjectId
from app.models import Cat
from dotenv import load_dotenv

from app.services.config_service import ConfigService



class CatService:
    def __init__(self, config_service: ConfigService):
        load_dotenv()
        config = config_service.get_config()
        self.client = MongoClient(host=config['mongodb_host'], 
                                              port=config['mongodb_port'], 
                                              username=config['mongodb_user'],
                                              password=config['mongodb_password'])
        self.db = self.client[config['mongodb_database_name']]
        self.cats = self.db.cats

    def create_cat(self, cat: Cat):
        result = self.cats.insert_one(cat.model_dump())
        return str(result.inserted_id)

    def get_cat(self, cat_id: str):
        cat = self.cats.find_one({"_id": ObjectId(cat_id)})
        if cat:
            cat['id'] = str(cat['_id'])
        return cat

    def update_cat(self, cat_id: str, cat: Cat):
        result = self.cats.update_one(
            {"_id": ObjectId(cat_id)},
            {"$set": cat.model_dump()}
        )
        return result.modified_count > 0

    def delete_cat(self, cat_id: str):
        result = self.cats.delete_one({"_id": ObjectId(cat_id)})
        return result.deleted_count > 0

    def list_cats(self):
        cats = self.cats.find()
        cat_list = []
        for cat in cats:
            cat_dict = {**cat}
            cat_dict["id"] = str(cat_dict.pop("_id"))
            cat_list.append(cat_dict)
        return cat_list
