from dataclasses import dataclass, field


@dataclass
class Oggetto:
    id: int
    nome: str
    tipo: str


@dataclass
class Inventario:
    id: int
    capacita_slot: int = 10
    oggetti: list[Oggetto] = field(default_factory=list)

    def aggiungi_oggetto(self, ogg: Oggetto) -> bool:
        if len(self.oggetti) < self.capacita_slot:
            self.oggetti.append(ogg)
            return True
        return False

    def rimuovi_oggetto_per_nome(self, nome: str) -> Oggetto | None:
        for idx, ogg in enumerate(self.oggetti):
            if ogg.nome.lower() == nome.lower():
                return self.oggetti.pop(idx)
        return None


@dataclass
class Personaggio:
    id: int
    nome: str
    inventario: Inventario | None = None

    def raccogli_oggetto(self, ogg: Oggetto) -> bool:
        if self.inventario is None:
            return False
        return self.inventario.aggiungi_oggetto(ogg)

    def usa_oggetto(self, nome: str) -> bool:
        if self.inventario is None:
            return False
        rimosso = self.inventario.rimuovi_oggetto_per_nome(nome)
        return rimosso is not None


def main() -> None:
    print("=== PRINCIPIO DI DELEGA (EROE -> ZAINO) ===")
    eroe = Personaggio(1, "Aragorn")
    pozione = Oggetto(10, "Pozione", "Cura")
    spada = Oggetto(20, "Spada", "Arma")

    print(f"Eroe senza zaino tenta raccolta -> Esito: {eroe.raccogli_oggetto(pozione)}\n")

    eroe.inventario = Inventario(101, capacita_slot=5)
    print("Equipaggiamento zaino completato!")

    es1 = eroe.raccogli_oggetto(pozione)
    es2 = eroe.raccogli_oggetto(spada)
    print(f"Eroe raccoglie Pozione -> Esito: {es1}")
    print(f"Eroe raccoglie Spada -> Esito: {es2}\n")

    es_uso1 = eroe.usa_oggetto("Pozione")
    print(f"Eroe usa Pozione -> Esito: {es_uso1} (oggetto rimosso dallo zaino)")

    es_uso2 = eroe.usa_oggetto("Scudo")
    print(f"Eroe tenta uso Scudo (non presente) -> Esito: {es_uso2}")


if __name__ == "__main__":
    main()
