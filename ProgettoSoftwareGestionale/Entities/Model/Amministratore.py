import os
import pickle

from Utente import Utente


class Amministratore(Utente):

    def __init__(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None, cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        super(Amministratore, self).__init__(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

    def _load(self):
        lista_amministratori_salvata = []
        if os.path.isfile('Data/amministratori.pickle'):
            with open('Data/amministratori.pickle', 'rb') as f:
                lista_amministratori_salvata = pickle.load(f)
        return lista_amministratori_salvata

    def _save(self, lista):
        with open('Data/amministratori.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_amministratore(self, anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia):
        super().aggiungiUtente(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

        lista_amministratori_salvata = self._load()
        lista_amministratori_salvata.append(self.get_info_amministratore())
        self._save(lista_amministratori_salvata)

    def get_info_amministratore(self):
        info = super().get_info_utente()
        return info

    def _from_dict(self, amministratore_dict):
        return Amministratore(
            amministratore_dict["anzianità"],
            amministratore_dict["cellulare"],
            amministratore_dict["codicefiscale"],
            amministratore_dict["codicemeccanografico"],
            amministratore_dict["cognome"],
            amministratore_dict["cra"],
            amministratore_dict["datanascita"],
            amministratore_dict["email"],
            amministratore_dict["nome"],
            amministratore_dict["password"],
            amministratore_dict["qualifica"],
            amministratore_dict["sezioneaia"]
        )

    def ricerca_utente_codicemeccanografico(self, codicemeccanografico):
        lista_amministratori_salvata = self._load()
        for amministratore_dict in lista_amministratori_salvata:
            if amministratore_dict["codicemeccanografico"] == codicemeccanografico:
                return self._from_dict(amministratore_dict)
        return None

    def ricerca_utente_nomecognome(self, nome, cognome):
        lista_amministratori_salvata = self._load()
        for amministratore_dict in lista_amministratori_salvata:
            if amministratore_dict["nome"] == nome and amministratore_dict["cognome"] == cognome:
                return self._from_dict(amministratore_dict)
        return None

    def rimuovi_amministratore(self):
        lista_amministratori_salvata = self._load()
        for amministratore in lista_amministratori_salvata:
            if amministratore["codicemeccanografico"] == self.codicemeccanografico:
                lista_amministratori_salvata.remove(amministratore)
                break
        self._save(lista_amministratori_salvata)

        super().rimuovi_utente()
        del self