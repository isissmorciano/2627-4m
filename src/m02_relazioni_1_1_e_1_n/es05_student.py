from dataclasses import dataclass, field


@dataclass
class ElementoCarrello:
    id_prodotto: int
    nome: str
    quantita: int
    prezzo_unitario: float

    def subtotale(self) -> float:
        # TODO: Restituisce quantita * prezzo_unitario arrotondato a 2 decimali.
        pass


@dataclass
class Carrello:
    id: int
    elementi: list[ElementoCarrello] = field(default_factory=list)

    def aggiungi_elemento(self, elemento: ElementoCarrello) -> None:
        # TODO: Aggiunge elemento a self.elementi.
        pass

    def rimuovi_prodotto(self, id_prodotto: int) -> bool:
        # TODO: Rimuove l'elemento con id_prodotto corrispondente e restituisce True. Se assente restituisce False.
        pass

    def calcola_totale(self) -> float:
        # TODO: Somma i subtotali di tutti gli elementi.
        pass


def main() -> None:
    # TODO: Simula aggiunta prodotti, calcolo totale, rimozione e ricalcolo.
    pass


if __name__ == "__main__":
    main()
