from dataclasses import dataclass


@dataclass
class CartellaClinica:
    numero_cartella: int
    diagnosi: str
    paziente: "Paziente | None" = None


@dataclass
class Paziente:
    codice_fiscale: str
    nome: str
    cartella: CartellaClinica | None = None

    def assegna_cartella(self, cartella: CartellaClinica) -> bool:
        # TODO: Se non ha cartella, collega reciprocamente e restituisci True, altrimenti False.
        pass

    def dimetti(self) -> bool:
        # TODO: Se ha cartella, azzera entrambi i riferimenti (None) e restituisci True, altrimenti False.
        pass


def main() -> None:
    # TODO: Simula assegnazione, rifiuto duplicato e dimissione.
    pass


if __name__ == "__main__":
    main()
