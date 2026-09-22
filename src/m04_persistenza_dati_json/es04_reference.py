import json
from dataclasses import dataclass, asdict


@dataclass
class Tessera:
    codice: str
    ingressi: int = 10

    def valida(self) -> bool:
        if self.ingressi > 0:
            self.ingressi -= 1
            return True
        return False


@dataclass
class Utente:
    id_utente: int
    nome: str
    tessera: Tessera | None = None


def salva_utente(u: Utente, percorso: str) -> None:
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(asdict(u), f, indent=4)


def carica_utente(percorso: str) -> Utente:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    dati_tessera = dati.pop("tessera", None)
    tessera_obj = Tessera(**dati_tessera) if dati_tessera else None
    return Utente(**dati, tessera=tessera_obj)


def main() -> None:
    print("=== DETECTIVE DELLA PERSISTENZA: RICOSTRUZIONE COMPLETA ===")
    file_path = "utente_tessera.json"
    utente_originale = Utente(1, "Mario Rossi", Tessera("T-999", ingressi=5))

    salva_utente(utente_originale, file_path)
    print("Salvataggio completato!\n")

    utente_ricaricato = carica_utente(file_path)
    print(f"Utente: {utente_ricaricato.nome}")
    print(f"Tessera associata e' una vera istanza? {isinstance(utente_ricaricato.tessera, Tessera)}")

    esito = utente_ricaricato.tessera.valida()
    print(f"Invocazione utente.tessera.valida() -> Esito: {esito}")
    print(f"Ingressi rimasti: {utente_ricaricato.tessera.ingressi}/5")


if __name__ == "__main__":
    main()
