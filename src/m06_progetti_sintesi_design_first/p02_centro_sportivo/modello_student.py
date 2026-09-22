from dataclasses import dataclass, field


@dataclass
class Attrezzatura:
    id: int
    nome: str
    tariffa_oraria: float


@dataclass
class NoleggioAttrezzatura:
    attrezzatura: Attrezzatura
    quantita: int

    def costo_noleggio(self) -> float:
        # TODO: Restituisce quantita * attrezzatura.tariffa_oraria
        pass


@dataclass
class Campo:
    codice_campo: str
    sport: str
    tariffa_oraria: float


@dataclass
class Prenotazione:
    id_prenotazione: int
    cliente: str
    campo: Campo
    data_ora: str
    noleggi: list[NoleggioAttrezzatura] = field(default_factory=list)

    def aggiungi_noleggio(self, att: Attrezzatura, quantita: int) -> None:
        # TODO: Aggiunge NoleggioAttrezzatura se quantita > 0
        pass

    def calcola_costo_totale(self) -> float:
        # TODO: campo.tariffa_oraria + somma di tutti i noleggi
        pass