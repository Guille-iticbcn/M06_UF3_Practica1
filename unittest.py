import unittest
from datetime import datetime
from AgendaEvent import AgendaEvent, MongoDBPersistence


class TestAgendaEvent(unittest.TestCase):
    def setUp(self):
        self.event = AgendaEvent("2024-04-16", 2, "Reunión de equipo", "descripcion", ["reunión", "equipo"], "Oficina")


    def test_getters(self):
        self.assertEqual(self.event.get_date(), "2024-04-16")
        self.assertEqual(self.event.get_duration(), 2)
        self.assertEqual(self.event.get_title(), "Reunión de equipo")
        self.assertEqual(self.event.get_description(), "descripcion")
        self.assertEqual(self.event.get_tags(), ["reunión", "equipo"])
        self.assertEqual(self.event.get_location(), "Oficina")


    def test_setters(self):
        self.event.set_date("2024-04-17")
        self.assertEqual(self.event.get_date(), "2024-04-17")
        
        self.event.set_duration(3)
        self.assertEqual(self.event.get_duration(), 3)
        
        self.event.set_title("Nuevo título")
        self.assertEqual(self.event.get_title(), "Nuevo título")
        
        self.event.set_description("Nueva descripción")
        self.assertEqual(self.event.get_description(), "Nueva descripción")
        
        self.event.set_tags(["nueva", "etiqueta"])
        self.assertEqual(self.event.get_tags(), ["nueva", "etiqueta"])
        
        self.event.set_location("Nueva ubicación")
        self.assertEqual(self.event.get_location(), "Nueva ubicación")


class TestMongoDBPersistence(unittest.TestCase):
    def setUp(self):
        self.persistence = MongoDBPersistence("mongodb://localhost:27017", "test_db", "test_collection")
        self.event_id = None


    def tearDown(self):
        if self.event_id:
            self.persistence.delete(self.event_id)


    def test_save_get_delete(self):
        event = AgendaEvent("2024-04-16", 2, "Reunión de equipo", "descripcion", ["reunión", "equipo"], "Oficina")
        self.event_id = self.persistence.save(event)
        retrieved_event = self.persistence.get(self.event_id)
        self.assertIsNotNone(retrieved_event)
        self.assertEqual(retrieved_event['date'], "2024-04-16")
        self.assertEqual(retrieved_event['duration'], 2)
        self.assertEqual(retrieved_event['title'], "Reunión de equipo")
        self.assertEqual(retrieved_event['description'], "descripcion")
        self.assertEqual(retrieved_event['tags'], ["reunión", "equipo"])
        self.assertEqual(retrieved_event['location'], "Oficina")
        
        self.persistence.delete(self.event_id)
        deleted_event = self.persistence.get(self.event_id)
        self.assertIsNone(deleted_event)


if __name__ == '__main__':
    unittest.main()