from dataclasses import dataclass


@dataclass
class CameraHotel:
    """Modella una camera d'albergo corretta e sicura."""

    numero_camera: int
    tipo: str
    tariffa_giornaliera: float
    is_occupata: bool = False

    def check_in(self) -> bool:
        if not self.is_occupata:
            self.is_occupata = True
            return True
        return False

    def check_out(self) -> bool:
        if self.is_occupata:
            self.is_occupata = False
            return True
        return False

    def applica_sconto(self, percentuale: float) -> bool:
        if 0 < percentuale <= 50.0:
            quota_sconto = (self.tariffa_giornaliera * percentuale) / 100.0
            self.tariffa_giornaliera = round(self.tariffa_giornaliera - quota_sconto, 2)
            return True
        return False


def main() -> None:
    print("=== TEST DIRETTO CAMERA HOTEL CORRETTA ===")
    camera = CameraHotel(numero_camera=101, tipo="Doppia", tariffa_giornaliera=120.0)
    print(
        f"Camera {camera.numero_camera} ({camera.tipo}) | Tariffa: {camera.tariffa_giornaliera:.2f}€ | Occupata: {camera.is_occupata}\n"
    )

    esito1 = camera.check_in()
    print(f"Primo check-in -> Esito: {esito1} (Stanza assegnata)")

    esito2 = camera.check_in()
    print(f"Secondo check-in consecutivo (errore) -> Esito: {esito2} (Stanza gia occupata!)\n")

    esito_sconto_vietato = camera.applica_sconto(70.0)
    print(f"Tentativo sconto 70% (fuori policy > 50%) -> Esito: {esito_sconto_vietato}")
    print(f"Tariffa inalterata: {camera.tariffa_giornaliera:.2f}€\n")

    esito_sconto_valido = camera.applica_sconto(20.0)
    print(f"Applicazione sconto consentito 20% -> Esito: {esito_sconto_valido}")
    print(f"Nuova tariffa scontata: {camera.tariffa_giornaliera:.2f}€\n")

    esito_out = camera.check_out()
    print(f"Check-out -> Esito: {esito_out} (Stanza liberata)")


if __name__ == "__main__":
    main()
