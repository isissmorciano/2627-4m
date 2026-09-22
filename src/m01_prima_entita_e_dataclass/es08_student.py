from dataclasses import dataclass


@dataclass
class CameraHotel:
    """ATTENZIONE: Questa implementazione contiene bug logici e violazioni di invarianti!
    Correggi il codice affinché rispetti tutte le specifiche di business."""

    numero_camera: int
    tipo: str
    tariffa_giornaliera: float
    is_occupata: bool = False

    def check_in(self) -> bool:
        # BUG: Il collega imposta ciecamente True senza verificare se la camera è già occupata!
        self.is_occupata = True
        return True

    def check_out(self) -> bool:
        # BUG: Il collega libera la stanza anche se era già libera!
        self.is_occupata = False
        return True

    def applica_sconto(self, percentuale: float) -> bool:
        # BUG: Non c'è limite massimo al 50% né controllo su percentuali negative!
        taglio = (self.tariffa_giornaliera * percentuale) / 100.0
        self.tariffa_giornaliera -= taglio
        return True


def main() -> None:
    # TODO: Implementa il test dimostrativo descritto nell'esempio di esecuzione.
    pass


if __name__ == "__main__":
    main()
