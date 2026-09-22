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
    if studente.credito_disponibile >= corso.prezzo_iscrizione:
        studente.credito_disponibile = round(studente.credito_disponibile - corso.prezzo_iscrizione, 2)
        return Iscrizione(id_iscrizione, studente, corso, data_str)
    return None


def main() -> None:
    print("=== PIATTAFORMA CORSI: PIPELINE COMPLETA ===")
    studente = Studente(1, "Marco", "marco@email.com", credito_disponibile=100.0)
    corso_python = Corso("PY-01", "Python Avanzato", 70.0)

    print(f"Studente: {studente.nome} (Credito iniziale: {studente.credito_disponibile:.2f}€)")
    print(f"Corso: {corso_python.titolo} (Prezzo: {corso_python.prezzo_iscrizione:.2f}€)\n")

    isc = iscrivi_studente_a_corso(101, studente, corso_python, "2026-10-15")
    print(f"Iscrizione -> Esito: {isc is not None}")
    print(f"Credito residuo studente: {studente.credito_disponibile:.2f}€")

    # Tentativo secondo corso senza credito
    corso_cloud = Corso("CL-02", "Cloud Architecture", 50.0)
    isc2 = iscrivi_studente_a_corso(102, studente, corso_cloud, "2026-10-16")
    print(f"Tentativo acquisto corso Cloud (50€) -> Esito: {isc2 is not None} (Credito insufficiente)")


if __name__ == "__main__":
    main()
