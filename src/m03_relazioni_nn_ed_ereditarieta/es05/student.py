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
        # TODO: Danno = 10 + self.forza. Infliggi al bersaglio e restituisci messaggio con ⚔️
        pass


class Mago(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, mana: int = 50, punti_vita: int = 80) -> None:
        super().__init__(id_personaggio, nome, punti_vita)
        self.mana = mana

    def attacca(self, bersaglio: Personaggio) -> str:
        # TODO: Se mana >= 15: consuma 15 mana, infliggi 25 danni con ✨. Altrimenti messaggio mana insufficiente.
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
