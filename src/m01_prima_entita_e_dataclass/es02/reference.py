from dataclasses import dataclass


@dataclass
class Personaggio:
    """Rappresenta un eroe nel gioco (approccio moderno con @dataclass)."""

    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100

    def presentati(self) -> str:
        return f"Sono {self.nome}, eroe di livello {self.livello} con {self.punti_vita} PV."


def main() -> None:
    print("=== TEST UGUAGLIANZA E RAPPRESENTAZIONE DATACLASS ===")
    eroe_a: Personaggio = Personaggio(id=1, nome="Aragorn")
    eroe_b: Personaggio = Personaggio(id=1, nome="Aragorn")
    eroe_c: Personaggio = Personaggio(id=2, nome="Legolas")

    print("Rappresentazione automatica eroe_a:")
    print(eroe_a)

    print("\nConfronto eroe_a == eroe_b (stessi dati):")
    print(eroe_a == eroe_b)

    print("\nConfronto eroe_a == eroe_c (dati diversi):")
    print(eroe_a == eroe_c)


if __name__ == "__main__":
    main()
