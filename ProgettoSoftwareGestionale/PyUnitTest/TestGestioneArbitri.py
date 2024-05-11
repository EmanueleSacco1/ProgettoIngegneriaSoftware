import unittest
from ProgettoSoftwareGestionale.Entities.Model.Amministratore import Amministratore

class TestAmministratore(unittest.TestCase):

    def setUp(self):
        self.amministratore = Amministratore()

    def test_aggiungi_arbitro(self):
        self.amministratore.aggiungi_arbitro('10', '987654321', 'PNCSLD32A01L120S',
                                             '123456789', 'Paniccia', 'Marche',
                                             '01-01-1932', 'osvaldopaniccia@hotmail.daje', 'Osvaldo',
                                             'password', 'AE', 'Macerata')
        self.assertEqual(len(self.amministratore._load()), 1)

    def test_ricerca_arbitro_codicemeccanografico(self):
        self.amministratore.aggiungi_arbitro('10', '987654321', 'PNCSLD32A01L120S',
                                             '123456789', 'Paniccia', 'Marche',
                                             '01-01-1932', 'osvaldopaniccia@hotmail.daje', 'Osvaldo',
                                             'password', 'AE', 'Macerata')
        arbitro = self.amministratore.ricerca_arbitro_codicemeccanografico('codicemeccanografico')
        self.assertIsNotNone(arbitro)

    def test_ricerca_arbitro_nomecognome(self):
        self.amministratore.aggiungi_arbitro('10', '987654321', 'PNCSLD32A01L120S',
                                             '123456789', 'Paniccia', 'Marche',
                                             '01-01-1932', 'osvaldopaniccia@hotmail.daje', 'Osvaldo',
                                             'password', 'AE', 'Macerata')
        arbitro = self.amministratore.ricerca_arbitro_nomecognome('nome', 'cognome')
        self.assertIsNotNone(arbitro)

    def test_rimuovi_arbitro(self):
        self.amministratore.aggiungi_arbitro('10', '987654321', 'PNCSLD32A01L120S',
                                             '123456789', 'Paniccia', 'Marche',
                                             '01-01-1932', 'osvaldopaniccia@hotmail.daje', 'Osvaldo',
                                             'password', 'AE', 'Macerata')
        self.amministratore.rimuovi_arbitro()
        self.assertEqual(len(self.amministratore._load()), 0)

if __name__ == '__main__':
    unittest.main()
