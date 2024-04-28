import unittest
from datetime import datetime
from agendaEvent import agendaEvent
from IPersistencia import *
from MongoDBPersistance import *
from Agenda import Agenda
from AgendaPersistance import *
from AgendaPersistenceInterface import *
from Usuari import *
from UsuariPersistance import *
from UsuariPersistenceInterface import *

class TestAgendaEvent(unittest.TestCase):

    def setUp(self):
        self.event = agendaEvent("2024-04-16", 2, "Reunión de equipo", "descripcion", ["reunión", "equipo"], "Oficina")

    def test_getters(self):
        self.assertEqual(self.event.get_fecha(), "2024-04-16")
        self.assertEqual(self.event.get_duracion(), 2)
        self.assertEqual(self.event.get_titulo(), "Reunión de equipo")
        self.assertEqual(self.event.get_descripcion(), "descripcion")
        self.assertEqual(self.event.get_tags(), ["reunión", "equipo"])
        self.assertEqual(self.event.get_ubicacion(), "Oficina")

    def test_setters(self):
        self.event.set_fecha("2024-04-17")
        self.event.set_duracion(3)
        self.event.set_titulo("Otra reunión")
        self.event.set_descripcion("Nueva descripción")
        self.event.set_tags(["nueva", "reunión"])
        self.event.set_ubicacion("Casa")

        self.assertEqual(self.event.get_fecha(), "2024-04-17")
        self.assertEqual(self.event.get_duracion(), 3)
        self.assertEqual(self.event.get_titulo(), "Otra reunión")
        self.assertEqual(self.event.get_descripcion(), "Nueva descripción")
        self.assertEqual(self.event.get_tags(), ["nueva", "reunión"])
        self.assertEqual(self.event.get_ubicacion(), "Casa")

class TestMongoDBInterface(unittest.TestCase):

    def setUp(self):
        self.db_interface = MongoDBInterface("mongodb+srv://2023guillermojaume:BJuxQ3eShBhktxam@cluster0.qw12na8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "test_db", "test_collection")

    def test_create_read_delete(self):
        # Test create
        record_data = {"name": "John", "age": 30}
        result = self.db_interface.create(record_data)
        self.assertTrue(result.acknowledged)
        self.assertIsNotNone(result.inserted_id)

        # Test read
        record = self.db_interface.read(result.inserted_id)
        self.assertEqual(record["name"], "John")
        self.assertEqual(record["age"], 30)

        # Test delete
        delete_result = self.db_interface.delete(result.inserted_id)
        self.assertEqual(delete_result.deleted_count, 1)

class TestMongoDBPersistence(unittest.TestCase):

    def setUp(self):
        self.db_persistence = MongoDBPersistence("mongodb+srv://2023guillermojaume:BJuxQ3eShBhktxam@cluster0.qw12na8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "test_db", "test_collection")

    def test_save_get_update_delete(self):
        # Test save
        event_id = self.db_persistence.save({
            "date": "2024-04-16",
            "duration": 2,
            "title": "Reunión de equipo",
            "description": "descripcion",
            "tags": ["reunión", "equipo"],
            "location": "Oficina"
        })
        self.assertIsNotNone(event_id)

        # Test get
        event = self.db_persistence.get(event_id)
        self.assertEqual(event["title"], "Reunión de equipo")
        self.assertEqual(event["description"], "descripcion")

        # Test update
        update_result = self.db_persistence.update(event_id, {
            "date": "2024-04-17",
            "duration": 3,
            "title": "Otra reunión",
            "description": "Nueva descripción",
            "tags": ["nueva", "reunión"],
            "location": "Casa"
        })
        self.assertEqual(update_result, 1)

        updated_event = self.db_persistence.get(event_id)
        self.assertEqual(updated_event["title"], "Otra reunión")
        self.assertEqual(updated_event["description"], "Nueva descripción")

        # Test delete
        delete_result = self.db_persistence.delete(event_id)
        self.assertEqual(delete_result, 1)

class TestUsuari(unittest.TestCase):
    def setUp(self):
        self.user = Usuari("Juan", "Perez", "Español")

    def test_getters(self):
        self.assertEqual(self.user.get_nom(), "Juan")
        self.assertEqual(self.user.get_cognom(), "Perez")
        self.assertEqual(self.user.get_nacionalitat(), "Español")

    def test_setters(self):
        self.user.set_nom("Pedro")
        self.user.set_cognom("Gomez")
        self.user.set_nacionalitat("Argentino")

        self.assertEqual(self.user.get_nom(), "Pedro")
        self.assertEqual(self.user.get_cognom(), "Gomez")
        self.assertEqual(self.user.get_nacionalitat(), "Argentino")


class TestUsuariPersistenceInterface(unittest.TestCase):
    def setUp(self):
        # Conexión a la base de datos de prueba
        self.client = MongoClient("mongodb+srv://2023guillermojaume:BJuxQ3eShBhktxam@cluster0.qw12na8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client["test_db"]
        self.collection = self.db["test_collection"]
        self.interface = UsuariPersistenceInterface(self.collection)

    def tearDown(self):
        # Limpiar la colección después de cada test
        self.collection.delete_many({})

    def test_create_read_delete_user(self):
        # Test create
        user_data = {"nom": "Juan", "cognom": "Perez", "nacionalitat": "Español"}
        result = self.interface.create_user(user_data)
        self.assertTrue(result.acknowledged)
        self.assertIsNotNone(result.inserted_id)

        # Test read
        user_id = str(result.inserted_id)
        user = self.interface.read_user(user_id)
        self.assertEqual(user["nom"], "Juan")
        self.assertEqual(user["cognom"], "Perez")
        self.assertEqual(user["nacionalitat"], "Español")

        # Test delete
        delete_result = self.interface.delete_user(user_id)
        self.assertEqual(delete_result.deleted_count, 1)


class TestAgendaMongoDBPersistence(unittest.TestCase):
    def setUp(self):
        # Conexión a la base de datos de prueba
        self.client = MongoClient("mongodb+srv://2023guillermojaume:BJuxQ3eShBhktxam@cluster0.qw12na8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client["test_db"]
        self.collection = self.db["test_collection"]
        self.persistence = AgendaMongoDBPersistence(self.collection)

    def tearDown(self):
        # Limpiar la colección después de cada test
        self.collection.delete_many({})

    def test_create_read_delete_agenda(self):
        # Test save
        agenda_data = {
            "date": "2024-04-16",
            "duration": 2,
            "title": "Reunión de equipo",
            "description": "descripcion",
            "tags": ["reunión", "equipo"],
            "location": "Oficina"
        }
        result = self.persistence.create_agenda(agenda_data)
        self.assertIsNotNone(result)

        # Test get
        agenda_id = str(result.inserted_id)
        agenda = self.persistence.read_agenda(agenda_id)
        self.assertEqual(agenda["title"], "Reunión de equipo")
        self.assertEqual(agenda["description"], "descripcion")

        # Test delete
        delete_result = self.persistence.delete_agenda(agenda_id)
        self.assertEqual(delete_result.deleted_count, 1)


if __name__ == '__main__':
    unittest.main()