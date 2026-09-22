import json
from dataclasses import asdict
from .modello_reference import Veicolo, Autovettura, Furgone, Manutenzione


def salva_flotta(veicoli: list[Veicolo], percorso: str) -> None:
    record = []
    for v in veicoli:
        dati = asdict(v)
        dati["tipo"] = "furgone" if isinstance(v, Furgone) else "auto"
        record.append(dati)

    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=4)


def carica_flotta(percorso: str) -> list[Veicolo]:
    with open(percorso, "r", encoding="utf-8") as f:
        record = json.load(f)

    flotta: list[Veicolo] = []
    for item in record:
        tipo = item.pop("tipo", "auto")
        dati_manut = item.pop("manutenzioni", [])
        manut_obj = [Manutenzione(**m) for m in dati_manut]

        if tipo == "furgone":
            flotta.append(Furgone(**item, manutenzioni=manut_obj))
        else:
            flotta.append(Autovettura(**item, manutenzioni=manut_obj))
    return flotta