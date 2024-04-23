from bson import ObjectId

from AgendaPersistenceInterface import AgendaPersistenceInterface


class AgendaMongoDBPersistence(AgendaPersistenceInterface):
    def __init__(self, db):
        super().__init__(db)

    def create_agenda(self, agenda_data):
        return self.collection.insert_one(agenda_data)

    def read_agenda(self, agenda_id):
        return self.collection.find_one({'_id': ObjectId(agenda_id)})

    def update_agenda(self, agenda_id, new_data):
        return self.collection.update_one({'_id': ObjectId(agenda_id)}, {'$set': new_data})

    def delete_agenda(self, agenda_id):
        return self.collection.delete_one({'_id': ObjectId(agenda_id)})
