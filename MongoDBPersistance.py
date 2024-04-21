from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBPersistence:
    def __init__(self, connection_string, db_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def save(self, event_dict):
        result = self.collection.insert_one(event_dict)
        return result.inserted_id
    
    def get(self, event_id):
        event_dict = self.collection.find_one({"_id": ObjectId(event_id)})
        return event_dict
    
    def update(self, event_id, event_dict):
        result = self.collection.update_one({"_id": ObjectId(event_id)}, {"$set": event_dict})
        return result.modified_count
    
    def delete(self, event_id):
        result = self.collection.delete_one({"_id": ObjectId(event_id)})
        return result.deleted_count
