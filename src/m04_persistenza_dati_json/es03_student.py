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
    # TODO: Per ogni eroe crea il dizionario con asdict(eroe).
    # TODO: Inserisci il discriminatore: 'tipo': 'guerriero' se isinstance(eroe, Guerriero) else 'mago' se isinstance(eroe, Mago) else 'base'.
    # TODO: Salva la lista di dizionari su JSON.
    pass


def carica_squadra(percorso: str) -> list[Personaggio]:
    # TODO: Carica la lista di dizionari dal JSON.
    # TODO: Per ogni elemento estrai 'tipo' con dati.pop('tipo').
    # TODO: Se tipo == 'guerriero' ritorna Guerriero(**dati), se 'mago' Mago(**dati), altrimenti Personaggio(**dati).
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
