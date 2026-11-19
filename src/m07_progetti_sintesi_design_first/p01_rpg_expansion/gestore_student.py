import json
from dataclasses import asdict
from .modello_student import Personaggio, Ladro, Inventario, Oggetto


def salva_partita(eroe: Personaggio, percorso: str) -> None:
    # TODO: Salva l'eroe con asdict, includendo 'is_ladro': isinstance(eroe, Ladro)
    pass


def carica_partita(percorso: str) -> Personaggio:
    # TODO: Ricostruisci inventario, oggetti e istanza corretta (Ladro o Personaggio)
    pass