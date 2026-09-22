# TODO: Importa il decoratore dataclass dal modulo dataclasses


# TODO: Decora la classe con @dataclass
class Personaggio:
    """Rappresenta un eroe nel gioco (approccio moderno con @dataclass)."""

    # TODO: Definisci i campi tipizzati:
    # id: int
    # nome: str
    # livello: int (default 1)
    # punti_vita: int (default 100)

    def presentati(self) -> str:
        # TODO: Restituisce 'Sono <nome>, eroe di livello <livello> con <punti_vita> PV.'
        pass


def main() -> None:
    # TODO: Crea eroe_a (id=1, nome='Aragorn') ed eroe_b (id=1, nome='Aragorn')
    # TODO: Crea eroe_c (id=2, nome='Legolas')
    # TODO: Stampa eroe_a per verificare __repr__ automatico
    # TODO: Stampa eroe_a == eroe_b (deve dare True)
    # TODO: Stampa eroe_a == eroe_c (deve dare False)
    pass


if __name__ == "__main__":
    main()
