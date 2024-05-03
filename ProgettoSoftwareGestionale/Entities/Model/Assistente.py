import os
import pickle

from Utente import Utente

class Assistente(Utente):

    def __init__(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None, cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        super(Assistente, self).__init__(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

    def _load(self):
        lista_assistenti_salvata = []
        if os.path.isfile('Data/assistenti.pickle'):
            with open('Data/assistenti.pickle', 'rb') as f:
                lista_assistenti_salvata = pickle.load(f)
        return lista_assistenti_salvata

    def _save(self, lista):
        with open('Data/assistenti.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def get_info_assistente(self):
        info = super().get_info_utente()
        return info

    def _from_dict(self, assistente_dict):
        return Assistente(
            assistente_dict["anzianità"],
            assistente_dict["cellulare"],
            assistente_dict["codicefiscale"],
            assistente_dict["codicemeccanografico"],
            assistente_dict["cognome"],
            assistente_dict["cra"],
            assistente_dict["datanascita"],
            assistente_dict["email"],
            assistente_dict["nome"],
            assistente_dict["password"],
            assistente_dict["qualifica"],
            assistente_dict["sezioneaia"]
        )
