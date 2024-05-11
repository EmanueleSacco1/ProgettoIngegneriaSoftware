import os
import pickle

from Utente import Utente


class Arbitro(Utente):

    def __init__(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None,
                 cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        super(Arbitro, self).__init__(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra,
                                      datanascita, email, nome, password, qualifica, sezioneaia)

    def _load(self):
        lista_arbitri_salvata = []
        if os.path.isfile('Data/arbitri.pickle'):
            with open('Data/arbitri.pickle', 'rb') as f:
                lista_arbitri_salvata = pickle.load(f)
        return lista_arbitri_salvata

    def _save(self, lista):
        with open('Data/arbitri.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def get_info_arbitro(self):
        info = super().get_info_utente()
        return info

    def _from_dict(self, arbitro_dict):
        return Arbitro(
            arbitro_dict["anzianità"],
            arbitro_dict["cellulare"],
            arbitro_dict["codicefiscale"],
            arbitro_dict["codicemeccanografico"],
            arbitro_dict["cognome"],
            arbitro_dict["cra"],
            arbitro_dict["datanascita"],
            arbitro_dict["email"],
            arbitro_dict["nome"],
            arbitro_dict["password"],
            arbitro_dict["qualifica"],
            arbitro_dict["sezioneaia"]
        )
