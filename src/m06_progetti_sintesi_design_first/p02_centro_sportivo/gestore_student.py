import json
from dataclasses import asdict
from .modello_student import Prenotazione, Campo, Attrezzatura, NoleggioAttrezzatura


def salva_prenotazione(prenotazione: Prenotazione, percorso: str) -> None:
    # TODO: Salva su file JSON formattato con asdict
    pass


def carica_prenotazione(percorso: str) -> Prenotazione:
    # TODO: Ricarica e ricostruisci intero grafo (Campo, Noleggi, Attrezzature)
    pass