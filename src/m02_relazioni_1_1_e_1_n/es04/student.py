from dataclasses import dataclass, field


@dataclass
class Oggetto:
    id: int
    nome: str
    tipo: str


@dataclass
class Inventario:
    id: int
    capacita_slot: int = 10
    oggetti: list[Oggetto] = field(default_factory=list)

    def aggiungi_oggetto(self, ogg: Oggetto) -> bool:
        if len(self.oggetti) < self.capacita_slot:
            self.oggetti.append(ogg)
            return True
        return False

    def rimuovi_oggetto_per_nome(self, nome: str) -> Oggetto | None:
        # TODO: Cerca l'oggetto con ogg.nome == nome, rimuovilo dalla lista e restituiscilo. Se assente restituisci None.
        pass


@dataclass
class Personaggio:
    id: int
    nome: str
    inventario: Inventario | None = None

    def raccogli_oggetto(self, ogg: Oggetto) -> bool:
        # TODO: Se inventario è None restituisci False, altrimenti delega a self.inventario.aggiungi_oggetto(ogg)
        pass

    def usa_oggetto(self, nome: str) -> bool:
        # TODO: Se inventario è None restituisci False, altrimenti delega la rimozione allo zaino.
        pass


def main() -> None:
    # TODO: Simula raccolta senza zaino, equipaggiamento, raccolta con delega e uso oggetto.
    pass


if __name__ == "__main__":
    main()
