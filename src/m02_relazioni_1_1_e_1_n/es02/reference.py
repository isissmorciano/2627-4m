from dataclasses import dataclass


@dataclass
class CartellaClinica:
    numero_cartella: int
    diagnosi: str
    paziente: "Paziente | None" = None


@dataclass
class Paziente:
    codice_fiscale: str
    nome: str
    cartella: CartellaClinica | None = None

    def assegna_cartella(self, cartella: CartellaClinica) -> bool:
        if self.cartella is None and cartella.paziente is None:
            self.cartella = cartella
            cartella.paziente = self
            return True
        return False

    def dimetti(self) -> bool:
        if self.cartella is not None:
            self.cartella.paziente = None
            self.cartella = None
            return True
        return False


def main() -> None:
    print("=== GESTIONALE CLINICA (RELAZIONE 1:1) ===")
    paz: Paziente = Paziente("RSSMRA80A01H501U", "Mario Rossi")
    cart: CartellaClinica = CartellaClinica(501, "Febbre persistente")

    print(f"Paziente: {paz.nome} (CF: {paz.codice_fiscale})")
    print(f"Cartella #{cart.numero_cartella} (Diagnosi: {cart.diagnosi})\n")

    esito = paz.assegna_cartella(cart)
    print(f"Assegnazione cartella -> Esito: {esito}")
    print(f"Verifica: {paz.nome} ha la cartella #{paz.cartella.numero_cartella}")
    print(f"Verifica: La cartella appartiene a {cart.paziente.nome}\n")

    esito_doppio = paz.assegna_cartella(CartellaClinica(502, "Altro"))
    print(f"Tentativo seconda assegnazione su stesso paziente -> Esito: {esito_doppio}\n")

    esito_dim = paz.dimetti()
    print(f"Dimissione paziente -> Esito: {esito_dim}")
    print("Stato post dimissione:")
    print(f"- Paziente cartella: {paz.cartella}")
    print(f"- Cartella proprietario: {cart.paziente}")


if __name__ == "__main__":
    main()
