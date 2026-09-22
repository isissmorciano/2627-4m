from dataclasses import dataclass


@dataclass
class BiciElettrica:
    """Modella una bicicletta elettrica con regole di noleggio e gestione batteria."""

    codice_telaio: str
    modello: str
    batteria_percentuale: int = 100
    is_noleggiata: bool = False

    def inizia_noleggio(self) -> bool:
        if not self.is_noleggiata and self.batteria_percentuale >= 20:
            self.is_noleggiata = True
            return True
        return False

    def termina_noleggio(self, consumo_batteria: int) -> bool:
        if self.is_noleggiata and consumo_batteria > 0:
            self.batteria_percentuale = max(0, self.batteria_percentuale - consumo_batteria)
            self.is_noleggiata = False
            return True
        return False

    def ricarica(self, percentuale: int) -> None:
        if percentuale > 0:
            self.batteria_percentuale = min(100, self.batteria_percentuale + percentuale)


def main() -> None:
    print("=== SIMULAZIONE BIKE SHARING GREENRIDE ===")
    bici: BiciElettrica = BiciElettrica(codice_telaio="BIKE-042", modello="CityPro", batteria_percentuale=25)
    print(
        f"Bici {bici.codice_telaio} ({bici.modello}) | Batteria: {bici.batteria_percentuale}% | Noleggiata: {bici.is_noleggiata}\n"
    )

    esito1 = bici.inizia_noleggio()
    print(f"Richiesta sblocco corsa -> Esito: {esito1}")
    print(f"Stato: Noleggiata: {bici.is_noleggiata} | Batteria: {bici.batteria_percentuale}%\n")

    esito2 = bici.termina_noleggio(15)
    print(f"Termine corsa (consumo 15%) -> Esito: {esito2}")
    print(f"Stato: Noleggiata: {bici.is_noleggiata} | Batteria residua: {bici.batteria_percentuale}%\n")

    esito3 = bici.inizia_noleggio()
    print(f"Tentativo nuovo noleggio -> Esito: {esito3}")
    print("Operazione rifiutata: batteria insufficiente (< 20%)!\n")

    bici.ricarica(50)
    print("Intervento operatore: ricarica +50%")
    print(
        f"Nuovo stato: Noleggiata: {bici.is_noleggiata} | Batteria: {bici.batteria_percentuale}% (Pronta per il noleggio)"
    )


if __name__ == "__main__":
    main()
