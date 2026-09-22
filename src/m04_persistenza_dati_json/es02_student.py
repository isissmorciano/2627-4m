import json
from dataclasses import dataclass, field, asdict


@dataclass
class Oggetto:
    id: int
    nome: str
    tipo: str


@dataclass
class Inventario:
    id: int
    capacita_slot: int = 10
    oggetti: list[Oggetto] = field(default_factory=list)


def salva_inventario(inv: Inventario, percorso: str) -> None:
    # TODO: Serializza con asdict e salva in JSON (indent=4, utf-8).
    pass


def carica_inventario(percorso: str) -> Inventario:
    # TODO: 1. Carica il JSON
    # TODO: 2. Estrai la lista dati_oggetti = dati.pop('oggetti', [])
    # TODO: 3. Ricostruisci ogni Oggetto con [Oggetto(**ogg) for ogg in dati_oggetti]
    # TODO: 4. Ritorna Inventario(**dati, oggetti=oggetti_ricostruiti)
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
