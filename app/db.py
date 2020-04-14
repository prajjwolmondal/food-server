from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

class DB():
    
    def set_pymongo_context(self, context):
        self.mongo = PyMongo(context)

    def add_user(self, user_dict: dict) -> str:
        user_data_collection = self.mongo.db.get_collection('user_data')
        insertResult = user_data_collection.insert_one(user_dict)
        return insertResult.inserted_id
        
    def get_user_by_id(self, user_id: str) -> dict:
        user_data_collection = self.mongo.db.get_collection('user_data')
        return user_data_collection.find_one({"_id" : ObjectId(user_id)})

    def get_user_by_username(self, username: str) -> dict:
        user_data_collection = self.mongo.db.get_collection('user_data')
        return user_data_collection.find_one({"username": username})

    def update_user_preferences(self, user_id: str, user_preferences_dict: dict):
        user_preferences_collection = self.mongo.db.get_collection('user_preferences')
        user_db_object = self.get_user_by_id(user_id)
        user_preferences_collection.update_one({'_id': user_db_object['_id']}, 
                                               {'$set': user_preferences_dict}, upsert=True)

    def get_user_preferences_document(self, user_id: str):
        user_preferences_collection = self.mongo.db.get_collection('user_preferences')
        return user_preferences_collection.find_one(ObjectId(user_id))