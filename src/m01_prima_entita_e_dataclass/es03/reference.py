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
        if danno > 0:
            self.punti_vita = max(0, self.punti_vita - danno)

    def cura(self, quantita: int) -> None:
        if quantita > 0:
            self.punti_vita = min(self.punti_vita_max, self.punti_vita + quantita)

    def is_vivo(self) -> bool:
        return self.punti_vita > 0


def main() -> None:
    print("=== SIMULAZIONE COMBATTIMENTO ED INVARIANTI ===")
    eroe: Personaggio = Personaggio(id=1, nome="Conan")
    print(f"Eroe creato: {eroe.nome} (PV: {eroe.punti_vita}/{eroe.punti_vita_max}, Vivo: {eroe.is_vivo()})\n")

    eroe.subisci_danno(40)
    print(f"Conan subisce 40 danni!\nPV attuali: {eroe.punti_vita}/{eroe.punti_vita_max}\n")

    eroe.cura(50)
    print(
        f"Conan beve una pozione da 50 PV!\nPV attuali (bloccati al massimo): {eroe.punti_vita}/{eroe.punti_vita_max}\n"
    )

    eroe.subisci_danno(150)
    print(
        f"Conan subisce un colpo critico da 150 danni!\nPV attuali (bloccati a zero): {eroe.punti_vita}/{eroe.punti_vita_max}"
    )
    print(f"Stato eroe: Conan è sconfitto? {not eroe.is_vivo()} (is_vivo: {eroe.is_vivo()})")


if __name__ == "__main__":
    main()
