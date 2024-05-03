class Utente():

    def __init__(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None, cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        self.anzianità = anzianità
        self.cellulare = cellulare
        self.codicefiscale = codicefiscale
        self.codicemeccanografico = codicemeccanografico
        self.cognome = cognome
        self.cra = cra
        self.datanascita = datanascita
        self.email = email
        self.nome = nome
        self.password = password
        self.qualifica = qualifica
        self.sezioneaia = sezioneaia

    def aggiungiUtente(self, anzianità, cellulare, codicefiscale, codicemeccanografico, cognome, cra, datanascita,
                 email, nome, password, qualifica, sezioneaia):
        self.anzianità = anzianità
        self.cellulare = cellulare
        self.codicefiscale = codicefiscale
        self.codicemeccanografico = codicemeccanografico
        self.cognome = cognome
        self.cra = cra
        self.datanascita = datanascita
        self.email = email
        self.nome = nome
        self.password = password
        self.qualifica = qualifica
        self.sezioneaia = sezioneaia

    def get_info_utente(self):
        return {
            "anzianità": self.anzianità,
            "cellulare": self.cellulare,
            "codicefiscale": self.codicefiscale,
            "codicemeccanografico": self.codicemeccanografico,
            "cognome": self.cognome,
            "cra": self.cra,
            "datanascita": self.datanascita,
            "email": self.email,
            "nome": self.nome,
            "password": self.password,
            "qualifica": self.qualifica,
            "sezioneaia": self.sezioneaia,
        }

    # Permette l'aggiornamento di tutti gli attributi dell'oggetto Utente (setinfoUtente)
    def setinfoUtente(self, anzianità=None, cellulare=None, codicefiscale=None, codicemeccanografico=None, cognome=None, cra=None, datanascita=None,
                 email=None, nome=None, password=None, qualifica=None, sezioneaia=None):
        self.anzianità = anzianità
        self.cellulare = cellulare
        self.codicefiscale = codicefiscale
        self.codicemeccanografico = codicemeccanografico
        self.cognome = cognome
        self.cra = cra
        self.datanascita = datanascita
        self.email = email
        self.nome = nome
        self.password = password
        self.qualifica = qualifica
        self.sezioneaia = sezioneaia
    def ricerca_utente_codicemeccanografico(self, codicemeccanografico):
        raise NotImplementedError()

    def ricerca_utente_nomecognome(self, nome, cognome):
        raise NotImplementedError()

    def rimuovi_utente(self):
        self.anzianità = None
        self.cellulare = None
        self.codicefiscale = None
        self.codicemeccanografico = None
        self.cognome = None
        self.cra = None
        self.datanascita = None
        self.email = None
        self.nome = None
        self.password = None
        self.qualifica = None
        self.sezioneaia = None


