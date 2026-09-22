class Utente:
    def __init__(self, id_utente: int, nome: str, email: str) -> None:
        self.id_utente = id_utente
        self.nome = nome
        self.email = email


class Docente(Utente):
    def __init__(self, id_utente: int, nome: str, email: str, tariffa_oraria: float) -> None:
        super().__init__(id_utente, nome, email)
        self.tariffa_oraria = tariffa_oraria


class Studente(Utente):
    def __init__(self, id_utente: int, nome: str, email: str, credito_disponibile: float = 0.0) -> None:
        super().__init__(id_utente, nome, email)
        self.credito_disponibile = credito_disponibile


class Corso:
    def __init__(self, codice: str, titolo: str, prezzo_iscrizione: float) -> None:
        self.codice = codice
        self.titolo = titolo
        self.prezzo_iscrizione = prezzo_iscrizione


class Iscrizione:
    def __init__(self, id_iscrizione: int, studente: Studente, corso: Corso, data_iscrizione: str) -> None:
        self.id_iscrizione = id_iscrizione
        self.studente = studente
        self.corso = corso
        self.data_iscrizione = data_iscrizione
        self.stato = "Attivo"


def iscrivi_studente_a_corso(id_iscrizione: int, studente: Studente, corso: Corso, data_str: str) -> Iscrizione | None:
    # TODO: Se studente.credito_disponibile >= corso.prezzo_iscrizione:
    # TODO: scala il prezzo dal credito e restituisci la nuova istanza Iscrizione.
    # TODO: Altrimenti restituisci None.
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
