from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    nome: str


@dataclass
class Corso:
    codice_corso: str
    titolo: str
    cfu: int


@dataclass
class Iscrizione:
    id: int
    studente: Studente
    corso: Corso
    data_iscrizione: str
    voto_esame: int | None = None

    def verbalizza_voto(self, voto: int) -> bool:
        # TODO: Se 18 <= voto <= 30 assegna a voto_esame e restituisci True, altrimenti False.
        pass

    def is_superato(self) -> bool:
        # TODO: Restituisce True se voto_esame non è None e >= 18, altrimenti False.
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
