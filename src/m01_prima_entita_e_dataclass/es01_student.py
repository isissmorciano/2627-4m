class Personaggio:
    """Classe base per rappresentare un eroe nel gioco (approccio tradizionale)."""

    def __init__(self, id_personaggio: int, nome: str, livello: int = 1) -> None:
        # TODO: Assegna gli attributi a self (id, nome, livello, punti_vita = 100)
        pass

    def presentati(self) -> str:
        # TODO: Restituisce 'Sono <nome>, eroe di livello <livello> con <punti_vita> PV.'
        pass

    def __str__(self) -> str:
        # TODO: Restituisce 'Personaggio #<id>: <nome> (PV: <punti_vita>/100)'
        pass


def main() -> None:
    # TODO: Crea eroe1 (id=1, 'Aragorn', livello=5) ed eroe2 (id=2, 'Legolas')
    # TODO: Stampa gli eroi con print() per testare __str__
    # TODO: Stampa l'output di presentati() per entrambi
    pass


if __name__ == "__main__":
    main()
