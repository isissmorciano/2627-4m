class Personaggio:
    def __init__(self, id_personaggio: int, nome: str, punti_vita: int = 100) -> None:
        self.id = id_personaggio
        self.nome = nome
        self.punti_vita = punti_vita


class Guerriero(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, forza: int, punti_vita: int = 120) -> None:
        super().__init__(id_personaggio, nome, punti_vita)
        self.forza = forza


class Mago(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, mana: int = 50, punti_vita: int = 80) -> None:
        super().__init__(id_personaggio, nome, punti_vita)
        self.mana = mana


def main() -> None:
    print("=== GERARCHIA EROI (IS-A) ===")
    conan: Guerriero = Guerriero(1, "Conan", forza=15, punti_vita=120)
    merlino: Mago = Mago(2, "Merlino", mana=50, punti_vita=80)

    print(f"Guerriero creato: {conan.nome} (ID: {conan.id}, PV: {conan.punti_vita}, Forza: {conan.forza})")
    print(f"Mago creato: {merlino.nome} (ID: {merlino.id}, PV: {merlino.punti_vita}, Mana: {merlino.mana})\n")

    print("Verifica polimorfica di tipo:")
    print(f"- Conan e' un Guerriero? {isinstance(conan, Guerriero)}")
    print(f"- Conan e' un Personaggio? {isinstance(conan, Personaggio)}")
    print(f"- Merlino e' un Mago? {isinstance(merlino, Mago)}")
    print(f"- Merlino e' un Personaggio? {isinstance(merlino, Personaggio)}")


if __name__ == "__main__":
    main()
