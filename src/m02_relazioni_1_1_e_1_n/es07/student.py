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
        pass

    def prenota_camera(self, tipo: str) -> Stanza | None:
        # TODO: Cerca la prima stanza del tipo specificato che sia is_occupata == False.
        # TODO: Se trovata, imposta is_occupata = True e restituiscila, altrimenti restituisci None.
        pass

    def conta_camere_libere(self) -> int:
        pass

    def incasso_massimo_giornaliero(self) -> float:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
