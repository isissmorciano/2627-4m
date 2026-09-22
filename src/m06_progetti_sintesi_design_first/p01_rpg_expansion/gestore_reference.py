import json
from dataclasses import asdict
from .modello_reference import Personaggio, Ladro, Inventario, Oggetto


def salva_partita(eroe: Personaggio, percorso: str) -> None:
    dati = asdict(eroe)
    dati["is_ladro"] = isinstance(eroe, Ladro)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)


def carica_partita(percorso: str) -> Personaggio:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    dati_inv = dati.pop("inventario", None)
    is_ladro = dati.pop("is_ladro", False)

    inv_obj = None
    if dati_inv:
        oggetti_dati = dati_inv.pop("oggetti", [])
        oggetti_obj = [Oggetto(**item) for item in oggetti_dati]
        inv_obj = Inventario(**dati_inv, oggetti=oggetti_obj)

    if is_ladro:
        return Ladro(**dati, inventario=inv_obj)
    return Personaggio(**dati, inventario=inv_obj)