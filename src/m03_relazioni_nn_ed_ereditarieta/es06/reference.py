class MetodoPagamento:
    def elabora(self, importo: float) -> tuple[bool, str]:
        return False, "Metodo generico non utilizzabile"


class CartaCredito(MetodoPagamento):
    def __init__(self, numero_carta: str, plafond_residuo: float) -> None:
        self.numero_carta = numero_carta
        self.plafond_residuo = plafond_residuo

    def elabora(self, importo: float) -> tuple[bool, str]:
        if importo <= self.plafond_residuo:
            self.plafond_residuo = round(self.plafond_residuo - importo, 2)
            return True, "Pagamento approvato con carta"
        return False, "Plafond carta insufficiente"


class BonificoBancario(MetodoPagamento):
    def __init__(self, iban: str, commissione_fissa: float = 1.50) -> None:
        self.iban = iban
        self.commissione_fissa = commissione_fissa

    def elabora(self, importo: float) -> tuple[bool, str]:
        totale = round(importo + self.commissione_fissa, 2)
        return True, f"Disposto bonifico di {totale:.2f}€ su IBAN {self.iban}"


def main() -> None:
    print("=== CASSA E-COMMERCE: PAGAMENTI POLIMORFICI ===")
    spesa = 100.0
    print(f"Carrello da pagare: {spesa:.2f}€\n")

    carta_insufficiente: CartaCredito = CartaCredito("1234-5678", plafond_residuo=50.0)
    carta_valida: CartaCredito = CartaCredito("1234-9999", plafond_residuo=200.0)
    bonifico: BonificoBancario = BonificoBancario("IT88X0123456789")

    es1, msg1 = carta_insufficiente.elabora(spesa)
    print(f"Tentativo 1 (Carta con 50€ plafond) -> Esito: {es1} | Messaggio: {msg1}")

    es2, msg2 = carta_valida.elabora(spesa)
    print(
        f"Tentativo 2 (Carta con 200€ plafond) -> Esito: {es2} | Messaggio: {msg2} (Plafond rimasto: {carta_valida.plafond_residuo}€)"
    )

    es3, msg3 = bonifico.elabora(spesa)
    print(f"Tentativo 3 (Bonifico con 1.50€ comm.) -> Esito: {es3} | Messaggio: {msg3}")


if __name__ == "__main__":
    main()
