from bson import ObjectId

from UsuariPersistenceInterface import UsuariPersistenceInterface

class UsuariMongoDBPersistence(UsuariPersistenceInterface):
    def __init__(self, db):
        super().__init__(db)

    def create_user(self, user_data):
        return self.collection.insert_one(user_data)

    def read_user(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})

    def update_user(self, user_id, new_data):
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': new_data})

    def delete_user(self, user_id):
        return self.collection.delete_one({'_id': ObjectId(user_id)})


