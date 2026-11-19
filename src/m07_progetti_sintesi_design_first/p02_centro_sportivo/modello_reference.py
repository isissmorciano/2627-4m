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
        return round(self.quantita * self.attrezzatura.tariffa_oraria, 2)


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
        if quantita > 0:
            self.noleggi.append(NoleggioAttrezzatura(att, quantita))

    def calcola_costo_totale(self) -> float:
        costo_campo = self.campo.tariffa_oraria
        costo_attrezzature = sum(item.costo_noleggio() for item in self.noleggi)
        return round(costo_campo + costo_attrezzature, 2)