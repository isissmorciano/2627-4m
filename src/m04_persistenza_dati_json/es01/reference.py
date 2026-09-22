import json
from dataclasses import dataclass, asdict


@dataclass
class Personaggio:
    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100

    def subisci_danno(self, danno: int) -> None:
        if danno > 0:
            self.punti_vita = max(0, self.punti_vita - danno)


def salva_personaggio(eroe: Personaggio, percorso: str) -> None:
    dati = asdict(eroe)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)


def carica_personaggio(percorso: str) -> Personaggio:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)
    return Personaggio(**dati)


def main() -> None:
    print("=== CICLO DI PERSISTENZA JSON: SINGOLA ENTITA ===")
    file_salvataggio = "salvataggio_eroe.json"
    eroe_originale = Personaggio(id=1, nome="Aragorn", livello=5, punti_vita=80)

    print(f"Eroe prima del salvataggio: {eroe_originale.nome} (Livello: {eroe_originale.livello}, PV: {eroe_originale.punti_vita})")
    salva_personaggio(eroe_originale, file_salvataggio)
    print(f"Salvataggio su '{file_salvataggio}' completato!\n")

    print("--- Riavvio simulato: ricaricamento da disco ---")
    eroe_ricaricato = carica_personaggio(file_salvataggio)
    print(f"Eroe ricaricato con successo: {eroe_ricaricato.nome} (Livello: {eroe_ricaricato.livello}, PV: {eroe_ricaricato.punti_vita})")

    eroe_ricaricato.subisci_danno(20)
    print(f"Verifica metodi: {eroe_ricaricato.nome} subisce 20 danni...")
    print(f"Nuovi PV: {eroe_ricaricato.punti_vita}/100 (L'oggetto e' vivo e operativo in RAM!)")


if __name__ == "__main__":
    main()
