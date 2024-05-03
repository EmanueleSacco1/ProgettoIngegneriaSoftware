import os
import pickle

from ProgettoSoftwareGestionale.Entities.Model import Utente
from ProgettoSoftwareGestionale.Entities.Model import Arbitro
from ProgettoSoftwareGestionale.Entities.Model import Assistente
from ProgettoSoftwareGestionale.Entities.Model import Osservatore

class Amministratore(Utente):

    def __init__(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None, cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        super(Amministratore, self).__init__(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

    def _load(self):
        lista_amministratori_salvata = []
        if os.path.isfile('../Data/amministratori.pickle'):
            with open('../Data/amministratori.pickle', 'rb') as f:
                lista_amministratori_salvata = pickle.load(f)
        return lista_amministratori_salvata

    def _save(self, lista):
        with open('../Data/amministratori.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_amministratore(self, anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia):
        super().aggiungiUtente(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

        lista_amministratori_salvata = self._load()
        lista_amministratori_salvata.append(self.get_info_amministratore())
        self._save(lista_amministratori_salvata)

    def rimuovi_amministratore(self):
        lista_amministratori_salvata = self._load()
        for amministratore in lista_amministratori_salvata:
            if amministratore["codicemeccanografico"] == self.codicemeccanografico:
                lista_amministratori_salvata.remove(amministratore)
                break
        self._save(lista_amministratori_salvata)

        super().rimuovi_utente()
        del self

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

    def ricerca_amministratore_codicemeccanografico(self, codicemeccanografico):
        lista_amministratori_salvata = self._load()
        for amministratore_dict in lista_amministratori_salvata:
            if amministratore_dict["codicemeccanografico"] == codicemeccanografico:
                return self._from_dict(amministratore_dict)
        return None

    def ricerca_amministratore_nomecognome(self, nome, cognome):
        lista_amministratori_salvata = self._load()
        for amministratore_dict in lista_amministratori_salvata:
            if amministratore_dict["nome"] == nome and amministratore_dict["cognome"] == cognome:
                return self._from_dict(amministratore_dict)
        return None

    def aggiungi_arbitro(self, anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia):
        super().aggiungiUtente(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia)

        lista_arbitri_salvata = self._load()
        lista_arbitri_salvata.append(self.get_info_arbitri())
        self._save(lista_arbitri_salvata)
    def ricerca_arbitro_codicemeccanografico(self, codicemeccanografico):
        lista_arbitri_salvata = self._load()
        for arbitro_dict in lista_arbitri_salvata:
            if arbitro_dict["codicemeccanografico"] == codicemeccanografico:
                return self._from_dict(arbitro_dict)
        return None

    def ricerca_arbitro_nomecognome(self, nome, cognome):
        lista_arbitri_salvata = self._load()
        for arbitro_dict in lista_arbitri_salvata:
            if arbitro_dict["nome"] == nome and arbitro_dict["cognome"] == cognome:
                return self._from_dict(arbitro_dict)
        return None

    def rimuovi_arbitro(self):
        lista_arbitri_salvata = self._load()
        for arbitro in lista_arbitri_salvata:
            if arbitro["codicemeccanografico"] == self.codicemeccanografico:
                lista_arbitri_salvata.remove(arbitro)
                break
        self._save(lista_arbitri_salvata)

        super().rimuovi_utente()
        del self

def aggiungi_assistente(self, anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
             email, nome, password, qualifica, sezioneaia):
    super().aggiungiUtente(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
             email, nome, password, qualifica, sezioneaia)

    lista_assistenti_salvata = self._load()
    lista_assistenti_salvata.append(self.get_info_assistenti())
    self._save(lista_assistenti_salvata)

def ricerca_assistente_codicemeccanografico(self, codicemeccanografico):
    lista_assistenti_salvata = self._load()
    for assistente_dict in lista_assistenti_salvata:
        if assistente_dict["codicemeccanografico"] == codicemeccanografico:
            return self._from_dict(assistente_dict)
    return None

def ricerca_assistente_nomecognome(self, nome, cognome):
    lista_assistenti_salvata = self._load()
    for assistente_dict in lista_assistenti_salvata:
        if assistente_dict["nome"] == nome and assistente_dict["cognome"] == cognome:
            return self._from_dict(assistente_dict)
    return None

def rimuovi_assistente(self):
    lista_assistenti_salvata = self._load()
    for assistente in lista_assistenti_salvata:
        if assistente["codicemeccanografico"] == self.codicemeccanografico:
            lista_assistenti_salvata.remove(assistente)
            break
    self._save(lista_assistenti_salvata)

    super().rimuovi_utente()
    del self

def aggiungi_osservatore(self, anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
             email, nome, password, qualifica, sezioneaia):
    super().aggiungiUtente(anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
             email, nome, password, qualifica, sezioneaia)

    lista_osservatori_salvata = self._load()
    lista_osservatori_salvata.append(self.get_info_osservatori())
    self._save(lista_osservatori_salvata)

def ricerca_osservatore_codicemeccanografico(self, codicemeccanografico):
    lista_osservatori_salvata = self._load()
    for osservatore_dict in lista_osservatori_salvata:
        if osservatore_dict["codicemeccanografico"] == codicemeccanografico:
            return self._from_dict(osservatore_dict)
    return None

def ricerca_osservatore_nomecognome(self, nome, cognome):
    lista_osservatori_salvata = self._load()
    for osservatore_dict in lista_osservatori_salvata:
        if osservatore_dict["nome"] == nome and osservatore_dict["cognome"] == cognome:
            return self._from_dict(osservatore_dict)
    return None

def rimuovi_osservatore(self):
    lista_osservatori_salvata = self._load()
    for osservatore in lista_osservatori_salvata:
        if osservatore["codicemeccanografico"] == self.codicemeccanografico:
            lista_osservatori_salvata.remove(osservatore)
            break
    self._save(lista_osservatori_salvata)

    super().rimuovi_utente()
    del self
