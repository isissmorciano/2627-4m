from dataclasses import dataclass, field


@dataclass
class Oggetto:
    id: int
    nome: str
    tipo: str


@dataclass
class Inventario:
    id: int
    capacita_slot: int = 20
    oggetti_contenuti: list[Oggetto] = field(default_factory=list)

    def aggiungi_oggetto(self, ogg: Oggetto) -> bool:
        if len(self.oggetti_contenuti) < self.capacita_slot:
            self.oggetti_contenuti.append(ogg)
            return True
        return False

    def conta_oggetti(self) -> int:
        return len(self.oggetti_contenuti)


def main() -> None:
    print("=== GESTIONE ZAINO (RELAZIONE 1:N) ===")
    zaino: Inventario = Inventario(id=1, capacita_slot=2)
    print(f"Zaino #1 creato (Capacita: {zaino.capacita_slot} slot | Oggetti iniziali: {zaino.conta_oggetti()})\n")

    es1 = zaino.aggiungi_oggetto(Oggetto(10, "Spada", "Arma"))
    print(f"Aggiunta Spada -> Esito: {es1} (Slot occupati: {zaino.conta_oggetti()}/{zaino.capacita_slot})")

    es2 = zaino.aggiungi_oggetto(Oggetto(20, "Pozione", "Cura"))
    print(f"Aggiunta Pozione -> Esito: {es2} (Slot occupati: {zaino.conta_oggetti()}/{zaino.capacita_slot})")

    es3 = zaino.aggiungi_oggetto(Oggetto(30, "Scudo", "Armatura"))
    print(f"Tentativo aggiunta Scudo (zaino pieno) -> Esito: {es3}")
    print(f"Slot occupati inalterati: {zaino.conta_oggetti()}/{zaino.capacita_slot}")


if __name__ == "__main__":
    main()
