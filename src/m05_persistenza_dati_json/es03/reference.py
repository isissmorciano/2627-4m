import json
from dataclasses import dataclass, asdict


@dataclass
class Personaggio:
    id: int
    nome: str

    def attacca(self) -> str:
        return f"{self.nome} attacca normalmente"


@dataclass
class Guerriero(Personaggio):
    forza: int = 10

    def attacca(self) -> str:
        return f"⚔️ {self.nome} sferra un colpo potente da {10 + self.forza} danni!"


@dataclass
class Mago(Personaggio):
    mana: int = 50

    def attacca(self) -> str:
        return f"✨ {self.nome} lancia un dardo magico da 25 danni!"


def salva_squadra(squadra: list[Personaggio], percorso: str) -> None:
    record = []
    for eroe in squadra:
        dati = asdict(eroe)
        if isinstance(eroe, Guerriero):
            dati["tipo"] = "guerriero"
        elif isinstance(eroe, Mago):
            dati["tipo"] = "mago"
        else:
            dati["tipo"] = "base"
        record.append(dati)

    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=4)


def carica_squadra(percorso: str) -> list[Personaggio]:
    with open(percorso, "r", encoding="utf-8") as f:
        record = json.load(f)

    risultato: list[Personaggio] = []
    for dati in record:
        tipo = dati.pop("tipo", "base")
        if tipo == "guerriero":
            risultato.append(Guerriero(**dati))
        elif tipo == "mago":
            risultato.append(Mago(**dati))
        else:
            risultato.append(Personaggio(**dati))
    return risultato


def main() -> None:
    print("=== PERSISTENZA POLIMORFICA (CAMPO DISCRIMINATORE) ===")
    file_path = "squadra.json"
    conan: Guerriero = Guerriero(1, "Conan", forza=12)
    merlino: Mago = Mago(2, "Merlino", mana=45)

    salva_squadra([conan, merlino], file_path)
    print("Salvataggio su 'squadra.json' completato!\n")

    print("--- Ricaricamento polimorfico ---")
    squadra_ricaricata = carica_squadra(file_path)

    for idx, e in enumerate(squadra_ricaricata, 1):
        info_spec = f"Forza: {e.forza}" if isinstance(e, Guerriero) else f"Mana: {e.mana}"
        print(f"{idx}. {e.nome} -> Tipo esatto: {type(e).__name__} | {info_spec}")

    print("\nVerifica polimorfismo post-ricarica:")
    for e in squadra_ricaricata:
        print(f"- {e.attacca()}")


if __name__ == "__main__":
    main()
