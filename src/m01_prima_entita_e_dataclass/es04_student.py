from dataclasses import dataclass


@dataclass
class ContoCorrente:
    """Modella un conto bancario proteggendo l'invariante di saldo non negativo."""

    iban: str
    titolare: str
    saldo: float = 0.0

    def deposita(self, importo: float) -> bool:
        # TODO: Se importo > 0 aggiungi a saldo e restituisci True, altrimenti restituisci False.
        pass

    def preleva(self, importo: float) -> bool:
        # TODO: Se importo > 0 e <= saldo sottrai e restituisci True, altrimenti restituisci False.
        pass

    def mostra_stato(self) -> str:
        # TODO: Restituisce 'Conto <iban> intestato a <titolare> - Saldo: <saldo:.2f>€'
        pass


def main() -> None:
    # TODO: Simula apertura conto, deposito, prelievo valido e tentativo di prelievo scoperto.
    pass


if __name__ == "__main__":
    main()
