class MetodoPagamento:
    def elabora(self, importo: float) -> tuple[bool, str]:
        return False, "Metodo generico non utilizzabile"


class CartaCredito(MetodoPagamento):
    def __init__(self, numero_carta: str, plafond_residuo: float) -> None:
        self.numero_carta = numero_carta
        self.plafond_residuo = plafond_residuo

    def elabora(self, importo: float) -> tuple[bool, str]:
        # TODO: Se importo <= plafond_residuo scala plafond e restituisci (True, 'Pagamento approvato con carta')
        # TODO: Altrimenti restituisci (False, 'Plafond carta insufficiente')
        pass


class BonificoBancario(MetodoPagamento):
    def __init__(self, iban: str, commissione_fissa: float = 1.50) -> None:
        self.iban = iban
        self.commissione_fissa = commissione_fissa

    def elabora(self, importo: float) -> tuple[bool, str]:
        # TODO: Calcola totale = importo + commissione_fissa e restituisci (True, f'Disposto bonifico di {totale:.2f}€ su IBAN {self.iban}')
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
