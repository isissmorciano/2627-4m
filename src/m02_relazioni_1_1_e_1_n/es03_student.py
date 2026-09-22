from dataclasses import dataclass, field


@dataclass
class Oggetto:
    id: int
    nome: str
    tipo: str


@dataclass
class Inventario:
    id: int
    capacita_slot: int = 20
    oggetti_contenuti: list[Oggetto] = field(default_factory=list)

    def aggiungi_oggetto(self, ogg: Oggetto) -> bool:
        # TODO: Se c'è spazio aggiungi a oggetti_contenuti e restituisci True, altrimenti False.
        pass

    def conta_oggetti(self) -> int:
        # TODO: Restituisce il numero di oggetti presenti.
        pass


def main() -> None:
    # TODO: Simula aggiunta oggetti e rifiuto a capienza esaurita.
    pass


if __name__ == "__main__":
    main()
