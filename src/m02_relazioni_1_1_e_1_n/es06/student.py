from dataclasses import dataclass, field


@dataclass
class Studente:
    matricola: int
    nome: str
    media_voti: float


@dataclass
class ClasseScolastica:
    sezione: str
    capienza_massima: int = 25
    studenti: list[Studente] = field(default_factory=list)

    def iscrivi_studente(self, s: Studente) -> bool:
        # TODO: Se c'è posto aggiungi e restituisci True, altrimenti False.
        pass

    def calcola_media_classe(self) -> float:
        # TODO: Calcola e restituisce la media dei voti (0.0 se vuota).
        pass

    def elenco_promossi(self) -> list[str]:
        # TODO: Restituisce la lista dei soli nomi con media_voti >= 6.0.
        pass


def main() -> None:
    # TODO: Simula iscrizioni, calcolo media ed elenco promossi.
    pass


if __name__ == "__main__":
    main()
