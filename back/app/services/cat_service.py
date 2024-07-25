from pymongo import MongoClient
from bson.objectid import ObjectId
from app.models import Cat

class CatService:
    def __init__(self, db_url: str, db_name: str):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.cats = self.db.cats

    def create_cat(self, cat: Cat):
        result = self.cats.insert_one(cat.model_dump())
        return str(result.inserted_id)

    def get_cat(self, cat_id: str):
        cat = self.cats.find_one({"_id": ObjectId(cat_id)})
        if cat:
            cat['_id'] = str(cat['_id'])
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
        return [{"_id": str(cat["_id"]), **cat} for cat in cats]
