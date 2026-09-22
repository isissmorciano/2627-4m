from dataclasses import dataclass


@dataclass
class Abilita:
    id: int
    nome_abilita: str
    costo_mana: int


@dataclass
class Personaggio:
    id: int
    nome: str


@dataclass
class AbilitaAppresa:
    """Entità di raccordo per la relazione N:N tra Personaggio e Abilità."""

    id: int
    personaggio: Personaggio
    abilita: Abilita
    livello_padronanza: int = 1

    def potenzia(self) -> None:
        # TODO: Incrementa livello_padronanza di 1 se è inferiore a 5.
        pass


def main() -> None:
    # TODO: Simula la creazione di 2 eroi, 1 abilità e 2 legami N:N indipendenti come nell'esempio.
    pass


if __name__ == "__main__":
    main()
