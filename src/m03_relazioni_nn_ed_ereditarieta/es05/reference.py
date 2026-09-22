class Personaggio:
    def __init__(self, id_personaggio: int, nome: str, punti_vita: int = 100) -> None:
        self.id = id_personaggio
        self.nome = nome
        self.punti_vita = punti_vita

    def subisci_danno(self, danno: int) -> None:
        if danno > 0:
            self.punti_vita = max(0, self.punti_vita - danno)

    def attacca(self, bersaglio: "Personaggio") -> str:
        danno = 10
        bersaglio.subisci_danno(danno)
        return f"{self.nome} infligge {danno} danni a {bersaglio.nome}."


class Guerriero(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, forza: int, punti_vita: int = 120) -> None:
        super().__init__(id_personaggio, nome, punti_vita)
        self.forza = forza

    def attacca(self, bersaglio: Personaggio) -> str:
        danno = 10 + self.forza
        bersaglio.subisci_danno(danno)
        return f"⚔️ {self.nome} sferra un colpo potente da {danno} danni su {bersaglio.nome}!"


class Mago(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, mana: int = 50, punti_vita: int = 80) -> None:
        super().__init__(id_personaggio, nome, punti_vita)
        self.mana = mana

    def attacca(self, bersaglio: Personaggio) -> str:
        if self.mana >= 15:
            self.mana -= 15
            danno = 25
            bersaglio.subisci_danno(danno)
            return f"✨ {self.nome} lancia un dardo magico da {danno} danni (Mana rimasto: {self.mana})!"
        return f"💨 {self.nome} non ha abbastanza mana per attaccare!"


def main() -> None:
    print("=== SIMULAZIONE POLIMORFISMO IN BATTAGLIA ===")
    conan: Guerriero = Guerriero(1, "Conan", forza=15)
    merlino: Mago = Mago(2, "Merlino", mana=50)
    orco: Personaggio = Personaggio(99, "Orco", punti_vita=100)

    squadra: list[Personaggio] = [conan, merlino]

    print(f"Bersaglio: {orco.nome} (PV: {orco.punti_vita})\n")
    print("Turno della squadra polimorfica:")
    for eroe in squadra:
        print(f"- {eroe.attacca(orco)}")

    print(f"\nStato finale {orco.nome}: PV {orco.punti_vita}/100")


if __name__ == "__main__":
    main()
