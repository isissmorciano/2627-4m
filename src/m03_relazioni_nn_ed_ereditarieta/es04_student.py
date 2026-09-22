class Personaggio:
    def __init__(self, id_personaggio: int, nome: str, punti_vita: int = 100) -> None:
        self.id = id_personaggio
        self.nome = nome
        self.punti_vita = punti_vita


class Guerriero(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, forza: int, punti_vita: int = 120) -> None:
        # TODO: Invoca super().__init__ per id, nome e punti_vita, poi assegna self.forza = forza
        pass


class Mago(Personaggio):
    def __init__(self, id_personaggio: int, nome: str, mana: int = 50, punti_vita: int = 80) -> None:
        # TODO: Invoca super().__init__ per id, nome e punti_vita, poi assegna self.mana = mana
        pass


def main() -> None:
    # TODO: Simula la creazione e verifica isinstance come nell'esempio.
    pass


if __name__ == "__main__":
    main()
