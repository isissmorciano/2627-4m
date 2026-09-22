from dataclasses import dataclass


@dataclass
class ContoCorrente:
    """Modella un conto bancario proteggendo l'invariante di saldo non negativo."""

    iban: str
    titolare: str
    saldo: float = 0.0

    def deposita(self, importo: float) -> bool:
        if importo > 0:
            self.saldo += importo
            return True
        return False

    def preleva(self, importo: float) -> bool:
        if 0 < importo <= self.saldo:
            self.saldo -= importo
            return True
        return False

    def mostra_stato(self) -> str:
        return f"Conto {self.iban} intestato a {self.titolare} - Saldo: {self.saldo:.2f}€"


def main() -> None:
    print("=== GESTIONALE CONTO CORRENTE ===")
    conto: ContoCorrente = ContoCorrente(iban="IT99X0123456789", titolare="Mario Rossi")
    print(conto.mostra_stato() + "\n")

    esito_dep = conto.deposita(250.0)
    print(f"Deposito 250.00€ -> Esito: {esito_dep}")
    print(conto.mostra_stato() + "\n")

    esito_prel = conto.preleva(100.0)
    print(f"Prelievo 100.00€ -> Esito: {esito_prel}")
    print(conto.mostra_stato() + "\n")

    esito_fallito = conto.preleva(300.0)
    print(f"Tentativo prelievo 300.00€ (scoperto) -> Esito: {esito_fallito}")
    print("Transazione negata per fondi insufficienti!")
    print(conto.mostra_stato())


if __name__ == "__main__":
    main()
