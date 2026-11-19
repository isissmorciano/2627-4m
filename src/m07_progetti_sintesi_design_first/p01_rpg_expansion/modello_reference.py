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


@dataclass
class Ladro(Personaggio):
    destrezza: int = 5

    def attacca(self, bersaglio: Personaggio) -> str:
        danno = 10 + (self.destrezza * 2)
        bersaglio.subisci_danno(danno)
        return f"🗡️ {self.nome} sferra un colpo furtivo da {danno} danni su {bersaglio.nome}!"


@dataclass
class Missione:
    id: int
    titolo: str
    ricompensa_base: int


@dataclass
class MissioneAccettata:
    id: int
    eroe: Personaggio
    missione: Missione
    stato: str = "In Corso"

    def completa_missione(self) -> None:
        if self.stato != "Completata":
            self.stato = "Completata"
            self.eroe.monete += self.missione.ricompensa_base