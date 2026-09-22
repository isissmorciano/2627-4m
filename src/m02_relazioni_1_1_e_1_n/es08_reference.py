from dataclasses import dataclass, field


@dataclass
class Giocatore:
    numero_maglia: int
    nome: str


@dataclass
class Squadra:
    nome_squadra: str
    giocatori: list[Giocatore] = field(default_factory=list)

    def aggiungi_giocatore(self, g: Giocatore) -> bool:
        if len(self.giocatori) < 11:
            self.giocatori.append(g)
            return True
        return False

    def conta_giocatori(self) -> int:
        return len(self.giocatori)


def main() -> None:
    print("=== TEST INDIPENDENZA SQUADRE ===")
    squadra_a = Squadra("Leoni")
    squadra_b = Squadra("Aquile")

    squadra_a.aggiungi_giocatore(Giocatore(10, "Messi"))

    print(f"Squadra A ({squadra_a.nome_squadra}) giocatori: {squadra_a.conta_giocatori()}")
    print(f"Squadra B ({squadra_b.nome_squadra}) giocatori: {squadra_b.conta_giocatori()}")

    if squadra_b.conta_giocatori() == 0:
        print("OK: Le due squadre sono indipendenti in memoria RAM!")


if __name__ == "__main__":
    main()
