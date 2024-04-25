import unittest
from datetime import datetime
from Agenda import Agenda
from AgendaPersistance import *
from AgendaPersistenceInterface import *
from Usuari import *
from UsuariPersistance import *
from UsuariPersistenceInterface import *

class testAgendaDigital(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()

    #TEST USUARI
    def setUp(self):
        self.usuari(Usuari("Guillero", "Jaume", "Español"))

    def getGetters(self):
        self.assertEqual(self.usuari.get_nom())