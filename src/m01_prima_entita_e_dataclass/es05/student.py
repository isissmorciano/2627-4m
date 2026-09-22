from dataclasses import dataclass


@dataclass
class TesseraAbbonamento:
    """Modella una tessera a ingressi scalari con stato di attivazione."""

    codice_tessera: str
    titolare: str
    ingressi_residui: int = 10
    is_attiva: bool = True

    def valida_accesso(self) -> bool:
        # TODO: Se is_attiva e ingressi_residui > 0: decrementa ingressi.
        # TODO: Se dopo il decremento ingressi_residui == 0, imposta is_attiva = False.
        # TODO: Restituisci True in caso di successo, False se accesso negato.
        pass

    def ricarica_ingressi(self, quantita: int) -> bool:
        # TODO: Se quantita > 0 aggiungi a ingressi_residui, riattiva tessera (is_attiva = True) e restituisci True.
        # TODO: Se quantita <= 0 restituisci False.
        pass

    def blocca_tessera(self) -> None:
        # TODO: Imposta is_attiva = False
        pass


def main() -> None:
    # TODO: Simula il ciclo del tornello dell'esempio di esecuzione (2 ingressi, esaurimento, blocco e ricarica).
    pass


if __name__ == "__main__":
    main()
