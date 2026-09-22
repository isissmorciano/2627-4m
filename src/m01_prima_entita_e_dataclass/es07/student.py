from dataclasses import dataclass


@dataclass
class BiciElettrica:
    """Modella una bicicletta elettrica con regole di noleggio e gestione batteria."""

    codice_telaio: str
    modello: str
    batteria_percentuale: int = 100
    is_noleggiata: bool = False

    def inizia_noleggio(self) -> bool:
        # TODO: Il noleggio è consentito solo se non noleggiata e batteria >= 20.
        # TODO: Se consentito, imposta is_noleggiata = True e restituisci True, altrimenti False.
        pass

    def termina_noleggio(self, consumo_batteria: int) -> bool:
        # TODO: Consentito solo se is_noleggiata è True e consumo > 0.
        # TODO: Riduci batteria_percentuale (senza scendere sotto 0), imposta is_noleggiata = False e restituisci True.
        # TODO: Altrimenti restituisci False.
        pass

    def ricarica(self, percentuale: int) -> None:
        # TODO: Se percentuale > 0 aumenta batteria_percentuale bloccandola al massimo a 100.
        pass


def main() -> None:
    # TODO: Simula il ciclo d'uso reale descritto nell'esempio di esecuzione.
    pass


if __name__ == "__main__":
    main()
