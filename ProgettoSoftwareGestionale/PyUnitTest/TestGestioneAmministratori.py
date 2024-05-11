import unittest
import os.path
import pickle
from ProgettoSoftwareGestionale.Entities.Model.Amministratore import Amministratore


class TestAmministratore(unittest.TestCase):

    def setUp(self):
        self.amministratore = Amministratore(anzianità='10', cellulare='987654321', codicefiscale='PNCSLD32A01L120S',
                                             codicemeccanografico='123456789',
                                             cognome='Paniccia', cra='Marche', datanascita='01-01-1932',
                                             email='osvaldopaniccia@hotmail.daje', nome='Osvaldo',
                                             password='password', qualifica='AE', sezioneaia='Macerata')

    def test_aggiungi_amministratore(self):
        self.amministratore.aggiungi_amministratore(anzianità='10', cellulare='987654321',
                                                    codicefiscale='PNCSLD32A01L120S',
                                                    codicemeccanografico='123456789',
                                                    cognome='Paniccia', cra='Marche', datanascita='01-01-1932',
                                                    email='osvaldopaniccia@hotmail.daje', nome='Osvaldo',
                                                    password='password', qualifica='AE',
                                                    sezioneaia='Macerata')
        lista_amministratori_salvata = self.amministratore._load()
        self.assertEqual(lista_amministratori_salvata[-1], self.amministratore.get_info_amministratore())

    def test_rimuovi_amministratore(self):
        self.amministratore.rimuovi_amministratore()
        lista_amministratori_salvata = self.amministratore._load()
        self.assertNotIn(self.amministratore.get_info_amministratore(), lista_amministratori_salvata)

    def tearDown(self):
        del self.amministratore


if __name__ == '__main__':
    unittest.main()
