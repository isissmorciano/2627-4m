import json
from dataclasses import asdict
from .modello_reference import Corso, Socio, Tessera, IscrizioneCorso


def salva_corso(corso: Corso, percorso: str) -> None:
    dati = asdict(corso)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)


def carica_corso(percorso: str) -> Corso:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    dati_iscrizioni = dati.pop("iscrizioni", [])
    iscrizioni_obj = []
    for item in dati_iscrizioni:
        dati_socio = item["socio"]
        tessera_obj = Tessera(**dati_socio["tessera"])
        socio_obj = Socio(dati_socio["codice_socio"], dati_socio["nome"], tessera_obj)
        iscrizioni_obj.append(IscrizioneCorso(item["id_iscrizione"], socio_obj, item["data"]))

    return Corso(**dati, iscrizioni=iscrizioni_obj)