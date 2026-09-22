from dataclasses import dataclass, field


@dataclass
class Stanza:
    numero: int
    tipo: str
    prezzo: float
    is_occupata: bool = False


@dataclass
class Hotel:
    nome: str
    stanze: list[Stanza] = field(default_factory=list)

    def aggiungi_stanza(self, s: Stanza) -> None:
        self.stanze.append(s)

    def prenota_camera(self, tipo: str) -> Stanza | None:
        for s in self.stanze:
            if s.tipo.lower() == tipo.lower() and not s.is_occupata:
                s.is_occupata = True
                return s
        return None

    def conta_camere_libere(self) -> int:
        return sum(1 for s in self.stanze if not s.is_occupata)

    def incasso_massimo_giornaliero(self) -> float:
        return round(sum(s.prezzo for s in self.stanze), 2)


def main() -> None:
    print("=== GESTIONALE HOTEL (PIPELINE 1:N) ===")
    hotel: Hotel = Hotel("Hotel Bellavista")
    hotel.aggiungi_stanza(Stanza(101, "Singola", 60.0))
    hotel.aggiungi_stanza(Stanza(102, "Doppia", 100.0))
    hotel.aggiungi_stanza(Stanza(103, "Doppia", 100.0))

    print(f"Camere libere iniziali: {hotel.conta_camere_libere()}/3")
    print(f"Incasso massimo potenziale: {hotel.incasso_massimo_giornaliero():.2f}€\n")

    assegnata = hotel.prenota_camera("Doppia")
    print(f"Prenotazione Doppia -> Assegnata camera #{assegnata.numero}")
    print(f"Camere libere rimaste: {hotel.conta_camere_libere()}/3")


if __name__ == "__main__":
    main()
