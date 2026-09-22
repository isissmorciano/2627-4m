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
        return self.abilita.danno_base * self.livello_padronanza

    def esegui_colpo(self) -> str:
        danno = self.calcola_potenza_effettiva()
        return f"{self.personaggio.nome} usa {self.abilita.nome_abilita} (Liv. {self.livello_padronanza}) infliggendo {danno} danni!"


def main() -> None:
    print("=== ESECUZIONE ABILITA APPRESA N:N ===")
    fulmine = Abilita(id=1, nome_abilita="Fulmine", danno_base=20, costo_mana=15)
    thor = Personaggio(id=10, nome="Thor")

    link = AbilitaAppresa(id=100, personaggio=thor, abilita=fulmine, livello_padronanza=3)

    print(f"Abilita creata: {fulmine.nome_abilita} (Danno Base: {fulmine.danno_base}, Costo: {fulmine.costo_mana})\n")
    print(f"Link: {link.personaggio.nome} apprende {link.abilita.nome_abilita} a livello {link.livello_padronanza}")
    print(f"Potenza effettiva calcolata: {link.calcola_potenza_effettiva()} danni (20 base * liv. 3)")
    print(f"Azione eseguita: {link.esegui_colpo()}")


if __name__ == "__main__":
    main()
