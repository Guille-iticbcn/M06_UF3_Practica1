import pymongo
from bson.objectid import ObjectId

class MongoDBInterface:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def create(self, record_data):
        return self.collection.insert_one(record_data)

    def read(self, record_id):
        return self.collection.find_one({'_id': ObjectId(record_id)})

    def read_all(self):
        return list(self.collection.find())

    def update(self, record_id, new_data):
        return self.collection.update_one({'_id': ObjectId(record_id)}, {'$set': new_data})

    def delete(self, record_id):
        return self.collection.delete_one({'_id': ObjectId(record_id)})
