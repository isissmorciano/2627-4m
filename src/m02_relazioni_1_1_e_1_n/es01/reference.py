from dataclasses import dataclass


@dataclass
class Inventario:
    """Modella lo zaino dell'eroe (lato della relazione 1:1)."""

    id: int
    capacita_slot: int = 20
    proprietario: "Personaggio | None" = None

    def imposta_proprietario(self, eroe: "Personaggio") -> None:
        self.proprietario = eroe


@dataclass
class Personaggio:
    """Modella l'eroe con il proprio inventario 1:1."""

    id: int
    nome: str
    livello: int = 1
    inventario: Inventario | None = None

    def assegna_inventario(self, inv: Inventario) -> None:
        self.inventario = inv
        inv.imposta_proprietario(self)


def main() -> None:
    print("=== ASSEGNAZIONE RELAZIONE 1:1 ===")
    eroe: Personaggio = Personaggio(id=1, nome="Aragorn")
    zaino: Inventario = Inventario(id=101, capacita_slot=30)

    print("Stato iniziale:")
    print(f"- Eroe: {eroe.nome} (Zaino: {eroe.inventario})")
    print(f"- Zaino #{zaino.id} (Proprietario: {zaino.proprietario})\n")

    print("Esecuzione: eroe.assegna_inventario(zaino)")
    eroe.assegna_inventario(zaino)
    print("Collegamento completato con successo!\n")

    print("Verifica navigazione bidirezionale:")
    if eroe.inventario is not None and zaino.proprietario is not None:
        print(f"- Da Eroe a Zaino: {eroe.nome} possiede uno zaino da {eroe.inventario.capacita_slot} slot.")
        print(f"- Da Zaino a Eroe: Lo zaino #{zaino.id} appartiene a: {zaino.proprietario.nome}")


if __name__ == "__main__":
    main()
