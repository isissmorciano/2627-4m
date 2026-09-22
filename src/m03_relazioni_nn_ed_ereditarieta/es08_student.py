class Motore:
    def __init__(self, cilindrata: int, tipo_carburante: str) -> None:
        self.cilindrata = cilindrata
        self.tipo_carburante = tipo_carburante


class Veicolo:
    def __init__(self, targa: str, marca: str, tariffa_base: float, motore: Motore | None = None) -> None:
        self.targa = targa
        self.marca = marca
        self.tariffa_base = tariffa_base
        self.motore = motore


class Furgone(Veicolo):
    def __init__(self, targa: str, marca: str, tariffa_base: float, capacita_carico_kg: int, motore: Motore | None = None) -> None:
        # BUG DEL COLLEGA: non usa super().__init__!
        # TODO: Correggi usando super().__init__(targa, marca, tariffa_base, motore)
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
