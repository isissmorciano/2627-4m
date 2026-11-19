import json
from dataclasses import dataclass, asdict


@dataclass
class Tessera:
    codice: str
    ingressi: int = 10

    def valida(self) -> bool:
        if self.ingressi > 0:
            self.ingressi -= 1
            return True
        return False


@dataclass
class Utente:
    id_utente: int
    nome: str
    tessera: Tessera | None = None


def salva_utente(u: Utente, percorso: str) -> None:
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(asdict(u), f, indent=4)


def carica_utente(percorso: str) -> Utente:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    # BUG DEL COLLEGA:
    # Ha scritto return Utente(**dati), lasciando dati['tessera'] come semplice dict!
    # TODO: Estrai dati_tessera = dati.pop('tessera', None)
    # TODO: Se presente ricostruisci tessera_obj = Tessera(**dati_tessera)
    # TODO: Ritorna Utente(**dati, tessera=tessera_obj)
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
