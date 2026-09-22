from dataclasses import dataclass, field


@dataclass
class ElementoCarrello:
    id_prodotto: int
    nome: str
    quantita: int
    prezzo_unitario: float

    def subtotale(self) -> float:
        return round(self.quantita * self.prezzo_unitario, 2)


@dataclass
class Carrello:
    id: int
    elementi: list[ElementoCarrello] = field(default_factory=list)

    def aggiungi_elemento(self, elemento: ElementoCarrello) -> None:
        self.elementi.append(elemento)

    def rimuovi_prodotto(self, id_prodotto: int) -> bool:
        for idx, item in enumerate(self.elementi):
            if item.id_prodotto == id_prodotto:
                self.elementi.pop(idx)
                return True
        return False

    def calcola_totale(self) -> float:
        return round(sum(item.subtotale() for item in self.elementi), 2)


def main() -> None:
    print("=== E-COMMERCE: CARRELLO SPESA (1:N) ===")
    carrello: Carrello = Carrello(id=1)
    e1: ElementoCarrello = ElementoCarrello(101, "Mouse", 2, 25.0)
    e2: ElementoCarrello = ElementoCarrello(102, "Tastiera", 1, 70.0)

    carrello.aggiungi_elemento(e1)
    carrello.aggiungi_elemento(e2)

    print(f"Aggiunto: {e1.nome} ({e1.quantita} x {e1.prezzo_unitario:.2f}€)")
    print(f"Aggiunto: {e2.nome} ({e2.quantita} x {e2.prezzo_unitario:.2f}€)")
    print(f"Totale carrello: {carrello.calcola_totale():.2f}€\n")

    esito_rim = carrello.rimuovi_prodotto(101)
    print(f"Rimozione Mouse (id=101) -> Esito: {esito_rim}")
    print(f"Nuovo totale carrello: {carrello.calcola_totale():.2f}€")


if __name__ == "__main__":
    main()
