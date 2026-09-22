import json
from dataclasses import dataclass, field, asdict


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


def salva_inventario(inv: Inventario, percorso: str) -> None:
    dati = asdict(inv)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)


def carica_inventario(percorso: str) -> Inventario:
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    dati_oggetti = dati.pop("oggetti", [])
    oggetti_ricostruiti = [Oggetto(**item) for item in dati_oggetti]
    return Inventario(**dati, oggetti=oggetti_ricostruiti)


def main() -> None:
    print("=== PERSISTENZA RELAZIONE 1:N (ZAINO E OGGETTI) ===")
    file_path = "inventario_test.json"
    zaino = Inventario(id=101, capacita_slot=5)
    zaino.oggetti.append(Oggetto(1, "Spada", "Arma"))
    zaino.oggetti.append(Oggetto(2, "Pozione", "Cura"))

    salva_inventario(zaino, file_path)
    print("Salvataggio zaino con 2 oggetti completato!\n")

    print("--- Ricaricamento e ricostruzione ---")
    ricaricato = carica_inventario(file_path)
    print(f"Zaino ricaricato #{ricaricato.id} (Capienza: {ricaricato.capacita_slot} slot)")
    print(f"Numero oggetti ricostruiti: {len(ricaricato.oggetti)}")

    for idx, ogg in enumerate(ricaricato.oggetti, 1):
        print(f"- Oggetto {idx}: {ogg.nome} (Tipo: {ogg.tipo}) -> isinstance(Oggetto): {isinstance(ogg, Oggetto)}")


if __name__ == "__main__":
    main()
