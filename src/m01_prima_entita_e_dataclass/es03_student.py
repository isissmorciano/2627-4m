from dataclasses import dataclass


@dataclass
class Personaggio:
    """Rappresenta un eroe che protegge i propri invarianti di salute."""

    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100
    punti_vita_max: int = 100

    def subisci_danno(self, danno: int) -> None:
        # TODO: Riduci punti_vita garantendo che non scendano mai sotto 0. Ignora danni <= 0.
        pass

    def cura(self, quantita: int) -> None:
        # TODO: Aumenta punti_vita garantendo che non superino punti_vita_max. Ignora cure <= 0.
        pass

    def is_vivo(self) -> bool:
        # TODO: Restituisce True se punti_vita > 0, altrimenti False.
        pass


def main() -> None:
    # TODO: Simula il combattimento dell'esempio di esecuzione (danno parziale, cura con limite, danno mortale).
    pass


if __name__ == "__main__":
    main()
