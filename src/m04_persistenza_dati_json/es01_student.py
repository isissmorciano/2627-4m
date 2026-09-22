import json
from dataclasses import dataclass, asdict


@dataclass
class Personaggio:
    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100

    def subisci_danno(self, danno: int) -> None:
        if danno > 0:
            self.punti_vita = max(0, self.punti_vita - danno)


def salva_personaggio(eroe: Personaggio, percorso: str) -> None:
    # TODO: Trasforma eroe in dizionario con asdict() e salvalo su file JSON (indent=4, utf-8).
    pass


def carica_personaggio(percorso: str) -> Personaggio:
    # TODO: Leggi il file JSON con json.load() e ricostruisci l'oggetto con Personaggio(**dati).
    pass


def main() -> None:
    # TODO: Simula creazione eroe, salvataggio, ricaricamento e invocazione di subisci_danno.
    pass


if __name__ == "__main__":
    main()
