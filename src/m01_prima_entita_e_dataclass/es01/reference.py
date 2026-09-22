class Personaggio:
    """Classe base per rappresentare un eroe nel gioco (approccio tradizionale)."""

    def __init__(self, id_personaggio: int, nome: str, livello: int = 1) -> None:
        self.id: int = id_personaggio
        self.nome: str = nome
        self.livello: int = livello
        self.punti_vita: int = 100

    def presentati(self) -> str:
        return f"Sono {self.nome}, eroe di livello {self.livello} con {self.punti_vita} PV."

    def __str__(self) -> str:
        return f"Personaggio #{self.id}: {self.nome} (PV: {self.punti_vita}/100)"


def main() -> None:
    print("=== CREAZIONE EROI RPG ===")
    eroe1: Personaggio = Personaggio(1, "Aragorn", livello=5)
    eroe2: Personaggio = Personaggio(2, "Legolas")

    print(eroe1)
    print(eroe2)

    print("\nPresentazione:")
    print(f"- {eroe1.presentati()}")
    print(f"- {eroe2.presentati()}")


if __name__ == "__main__":
    main()
