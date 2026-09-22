from dataclasses import dataclass, field


@dataclass
class Manutenzione:
    id: int
    data: str
    descrizione: str
    costo: float


@dataclass
class Veicolo:
    targa: str
    marca: str
    tariffa_base: float
    is_disponibile: bool = True
    manutenzioni: list[Manutenzione] = field(default_factory=list)

    def calcola_canone_giornaliero(self) -> float:
        return self.tariffa_base

    def registra_manutenzione(self, m: Manutenzione) -> None:
        self.manutenzioni.append(m)


@dataclass
class Autovettura(Veicolo):
    numero_posti: int = 5


@dataclass
class Furgone(Veicolo):
    capacita_quintali: int = 10

    def calcola_canone_giornaliero(self) -> float:
        # TODO: tariffa_base + (capacita_quintali * 5.0)
        pass