import json
from dataclasses import asdict
from .modello_reference import Prenotazione, Campo, Attrezzatura, NoleggioAttrezzatura


def salva_prenotazione(prenotazione: Prenotazione, percorso: str) -> None:
    dati = asdict(prenotazione)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)


def carica_prenotazione(percorso: str) -> Prenotazione:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    dati_campo = dati.pop("campo")
    campo_obj = Campo(**dati_campo)

    dati_noleggi = dati.pop("noleggi", [])
    noleggi_obj = []
    for item in dati_noleggi:
        att_obj = Attrezzatura(**item["attrezzatura"])
        noleggi_obj.append(NoleggioAttrezzatura(att_obj, item["quantita"]))

    return Prenotazione(**dati, campo=campo_obj, noleggi=noleggi_obj)