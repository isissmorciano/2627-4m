from dataclasses import dataclass, field


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

    def aggiungi(self, ogg: Oggetto) -> bool:
        if len(self.oggetti) < self.capacita_slot:
            self.oggetti.append(ogg)
            return True
        return False


@dataclass
class Personaggio:
    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100
    monete: int = 0
    inventario: Inventario | None = None

    def subisci_danno(self, danno: int) -> None:
        if danno > 0:
            self.punti_vita = max(0, self.punti_vita - danno)

    def attacca(self, bersaglio: "Personaggio") -> str:
        danno = 10
        bersaglio.subisci_danno(danno)
        return f"{self.nome} infligge {danno} danni a {bersaglio.nome}."


# TODO: Implementa la classe Ladro che eredita da Personaggio
# Attributo specifico: destrezza: int = 5
# Override di attacca(bersaglio): danno = 10 + (self.destrezza * 2), messaggio con 🗡️
@dataclass
class Ladro(Personaggio):
    pass


@dataclass
class Missione:
    id: int
    titolo: str
    ricompensa_base: int


# TODO: Implementa l'entità di raccordo MissioneAccettata
# Campi: id, eroe, missione, stato = 'In Corso'
# Metodo: completa_missione() -> imposta stato = 'Completata' e aggiunge eroe.monete += missione.ricompensa_base
@dataclass
class MissioneAccettata:
    pass