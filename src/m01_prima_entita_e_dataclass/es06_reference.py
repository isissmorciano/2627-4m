from dataclasses import dataclass


@dataclass
class ArticoloMagazzino:
    """Modella un articolo a magazzino proteggendo la giacenza da rotture di stock."""

    codice_sku: str
    nome: str
    prezzo_unitario: float
    quantita_disponibile: int = 0
    scorta_minima: int = 5

    def scarica(self, quantita: int) -> bool:
        if 0 < quantita <= self.quantita_disponibile:
            self.quantita_disponibile -= quantita
            return True
        return False

    def rifornisci(self, quantita: int) -> bool:
        if quantita > 0:
            self.quantita_disponibile += quantita
            return True
        return False

    def sotto_scorta(self) -> bool:
        return self.quantita_disponibile <= self.scorta_minima

    def valore_inventario(self) -> float:
        return round(self.quantita_disponibile * self.prezzo_unitario, 2)


def main() -> None:
    print("=== GESTIONE SCORTE MAGAZZINO ===")
    art = ArticoloMagazzino(
        codice_sku="SKU-TECH-01",
        nome="Tastiera Meccanica",
        prezzo_unitario=75.0,
        quantita_disponibile=12,
        scorta_minima=5,
    )

    print(f"Articolo {art.codice_sku}: {art.nome}")
    print(
        f"Prezzo: {art.prezzo_unitario:.2f}€ | Giacenza: {art.quantita_disponibile} pezzi | Scorta Minima: {art.scorta_minima}"
    )
    print(f"Valore inventario iniziale: {art.valore_inventario():.2f}€ | Sotto scorta? {art.sotto_scorta()}\n")

    esito_scarico = art.scarica(8)
    print(f"Scarico 8 pezzi (vendita) -> Esito: {esito_scarico}")
    print(f"Nuova giacenza: {art.quantita_disponibile} pezzi")
    if art.sotto_scorta():
        print(f"ATTENZIONE: Articolo sotto scorta! (sotto_scorta: {art.sotto_scorta()})\n")

    esito_negato = art.scarica(10)
    print(f"Tentativo scarico 10 pezzi (richiesta oltre stock) -> Esito: {esito_negato}")
    print("Operazione respinta: merce insufficiente!")
    print(f"Giacenza inalterata: {art.quantita_disponibile} pezzi\n")

    esito_rif = art.rifornisci(20)
    print(f"Rifornimento fornitore (+20 pezzi) -> Esito: {esito_rif}")
    print(f"Nuova giacenza: {art.quantita_disponibile} pezzi | Sotto scorta? {art.sotto_scorta()}")
    print(f"Valore inventario aggiornato: {art.valore_inventario():.2f}€")


if __name__ == "__main__":
    main()
