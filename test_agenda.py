import unittest
from datetime import datetime
from agendaEvent import agendaEvent
from IPersistencia import *
from MongoDBPersistance import *

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

if __name__ == '__main__':
    unittest.main()