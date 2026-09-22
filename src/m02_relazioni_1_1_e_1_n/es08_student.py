from dataclasses import dataclass, field


@dataclass
class Giocatore:
    numero_maglia: int
    nome: str


@dataclass
class Squadra:
    nome_squadra: str
    # BUG DEL COLLEGA: Ha scritto giocatori: list[Giocatore] = []
    # Correggi usando field(default_factory=list)
    giocatori: list[Giocatore] = field(default_factory=list)

    def aggiungi_giocatore(self, g: Giocatore) -> bool:
        # TODO: Se len(giocatori) < 11 aggiungi e restituisci True, altrimenti False.
        pass

    def conta_giocatori(self) -> int:
        return len(self.giocatori)


def main() -> None:
    # TODO: Dimostra che due squadre diverse non condividono i giocatori.
    pass


if __name__ == "__main__":
    main()
