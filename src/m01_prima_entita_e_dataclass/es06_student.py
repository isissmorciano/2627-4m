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
        # TODO: Se 0 < quantita <= quantita_disponibile sottrai e restituisci True, altrimenti False.
        pass

    def rifornisci(self, quantita: int) -> bool:
        # TODO: Se quantita > 0 aggiungi a quantita_disponibile e restituisci True, altrimenti False.
        pass

    def sotto_scorta(self) -> bool:
        # TODO: Restituisce True se quantita_disponibile <= scorta_minima, altrimenti False.
        pass

    def valore_inventario(self) -> float:
        # TODO: Restituisce il valore economico complessivo a magazzino (quantita * prezzo) arrotondato a 2 decimali.
        pass


def main() -> None:
    # TODO: Simula il flusso di magazzino dell'esempio di esecuzione (scarico, sottoscorta, rifiuto, rifornimento).
    pass


if __name__ == "__main__":
    main()
