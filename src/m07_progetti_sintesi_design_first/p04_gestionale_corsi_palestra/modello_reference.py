from dataclasses import dataclass, field


@dataclass
class Tessera:
    codice: str
    ingressi: int = 10
    is_attiva: bool = True

    def consuma_ingresso(self) -> bool:
        if self.is_attiva and self.ingressi > 0:
            self.ingressi -= 1
            if self.ingressi == 0:
                self.is_attiva = False
            return True
        return False


@dataclass
class Socio:
    codice_socio: str
    nome: str
    tessera: Tessera


@dataclass
class IscrizioneCorso:
    id_iscrizione: int
    socio: Socio
    data: str


@dataclass
class Corso:
    codice: str
    titolo: str
    capienza_massima: int = 15
    iscrizioni: list[IscrizioneCorso] = field(default_factory=list)

    def iscrivi_socio(self, id_iscrizione: int, socio: Socio, data_str: str) -> bool:
        if len(self.iscrizioni) >= self.capienza_massima:
            return False

        if socio.tessera.consuma_ingresso():
            self.iscrizioni.append(IscrizioneCorso(id_iscrizione, socio, data_str))
            return True
        return False