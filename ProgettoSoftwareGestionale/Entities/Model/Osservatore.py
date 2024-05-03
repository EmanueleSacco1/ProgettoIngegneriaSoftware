import os
import pickle

from Utente import Utente

class Osservatore(Utente):

    def __init__(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None, cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        super(Osservatore, self).__init__(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

    def _load(self):
        lista_osservatori_salvata = []
        if os.path.isfile('Data/osservatori.pickle'):
            with open('Data/osservatori.pickle', 'rb') as f:
                lista_osservatori_salvata = pickle.load(f)
        return lista_osservatori_salvata

    def _save(self, lista):
        with open('Data/osservatori.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def get_info_osservatore(self):
        info = super().get_info_utente()
        return info

    def _from_dict(self, osservatore_dict):
        return Osservatore(
            osservatore_dict["anzianità"],
            osservatore_dict["cellulare"],
            osservatore_dict["codicefiscale"],
            osservatore_dict["codicemeccanografico"],
            osservatore_dict["cognome"],
            osservatore_dict["cra"],
            osservatore_dict["datanascita"],
            osservatore_dict["email"],
            osservatore_dict["nome"],
            osservatore_dict["password"],
            osservatore_dict["qualifica"],
            osservatore_dict["sezioneaia"]
        )
