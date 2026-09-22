from dataclasses import dataclass


@dataclass
class TesseraAbbonamento:
    """Modella una tessera a ingressi scalari con stato di attivazione."""

    codice_tessera: str
    titolare: str
    ingressi_residui: int = 10
    is_attiva: bool = True

    def valida_accesso(self) -> bool:
        if self.is_attiva and self.ingressi_residui > 0:
            self.ingressi_residui -= 1
            if self.ingressi_residui == 0:
                self.is_attiva = False
            return True
        return False

    def ricarica_ingressi(self, quantita: int) -> bool:
        if quantita > 0:
            self.ingressi_residui += quantita
            self.is_attiva = True
            return True
        return False

    def blocca_tessera(self) -> None:
        self.is_attiva = False


def main() -> None:
    print("=== SIMULAZIONE CONTROLLO ACCESSI TORNELLO ===")
    tessera = TesseraAbbonamento(codice_tessera="CARD-555", titolare="Laura Verdi", ingressi_residui=2)
    print(
        f"Tessera {tessera.codice_tessera} (Titolare: {tessera.titolare}, Ingressi: {tessera.ingressi_residui}, Attiva: {tessera.is_attiva})\n"
    )

    esito1 = tessera.valida_accesso()
    print(f"Convalida 1 -> Esito: {esito1} (Passaggio concesso)")
    print(f"Stato: {tessera.ingressi_residui} ingressi residui, Attiva: {tessera.is_attiva}\n")

    esito2 = tessera.valida_accesso()
    print(f"Convalida 2 -> Esito: {esito2} (Passaggio concesso)")
    print("Attenzione: ingressi esauriti, tessera disattivata!")
    print(f"Stato: {tessera.ingressi_residui} ingressi residui, Attiva: {tessera.is_attiva}\n")

    esito3 = tessera.valida_accesso()
    print(f"Convalida 3 -> Esito: {esito3} (Accesso negato al tornello!)")
    print(f"Stato: {tessera.ingressi_residui} ingressi residui, Attiva: {tessera.is_attiva}\n")

    esito_ric = tessera.ricarica_ingressi(5)
    print(f"Ricarica di 5 ingressi in cassa -> Esito: {esito_ric}")
    print(f"Stato: {tessera.ingressi_residui} ingressi residui, Attiva: {tessera.is_attiva}")


if __name__ == "__main__":
    main()
