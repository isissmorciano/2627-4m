from dataclasses import dataclass


@dataclass
class Inventario:
    """Modella lo zaino dell'eroe (lato della relazione 1:1)."""

    id: int
    capacita_slot: int = 20
    proprietario: "Personaggio | None" = None

    def imposta_proprietario(self, eroe: "Personaggio") -> None:
        # TODO: Salva eroe in self.proprietario
        pass


@dataclass
class Personaggio:
    """Modella l'eroe con il proprio inventario 1:1."""

    id: int
    nome: str
    livello: int = 1
    inventario: Inventario | None = None

    def assegna_inventario(self, inv: Inventario) -> None:
        # TODO: Salva inv in self.inventario e invoca inv.imposta_proprietario(self)
        pass


def main() -> None:
    # TODO: Simula l'assegnazione 1:1 e verifica la navigazione bidirezionale come nell'esempio.
    pass


if __name__ == "__main__":
    main()
