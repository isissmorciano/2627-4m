from dataclasses import dataclass


@dataclass
class Abilita:
    id: int
    nome_abilita: str
    danno_base: int
    costo_mana: int


@dataclass
class Personaggio:
    id: int
    nome: str


@dataclass
class AbilitaAppresa:
    id: int
    personaggio: Personaggio
    abilita: Abilita
    livello_padronanza: int = 1

    def calcola_potenza_effettiva(self) -> int:
        # TODO: Restituisce danno_base * livello_padronanza
        pass

    def esegui_colpo(self) -> str:
        # TODO: Restituisce '<nome_eroe> usa <nome_abilita> (Liv. <padronanza>) infliggendo <danno> danni!'
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
