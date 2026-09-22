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
    id: int
    personaggio: Personaggio
    abilita: Abilita
    livello_padronanza: int = 1

    def potenzia(self) -> None:
        if self.livello_padronanza < 5:
            self.livello_padronanza += 1


def main() -> None:
    print("=== RELAZIONE MOLTI-A-MOLTI: EROI ED ABILITA ===")
    aragorn: Personaggio = Personaggio(1, "Aragorn")
    merlino: Personaggio = Personaggio(2, "Merlino")
    fuoco: Abilita = Abilita(10, "Palla di Fuoco", costo_mana=25)

    link_aragorn: AbilitaAppresa = AbilitaAppresa(101, aragorn, fuoco, livello_padronanza=1)
    link_merlino: AbilitaAppresa = AbilitaAppresa(102, merlino, fuoco, livello_padronanza=3)

    print(f"Eroi: {aragorn.nome} (id={aragorn.id}), {merlino.nome} (id={merlino.id})")
    print(f"Abilita create: {fuoco.nome_abilita} (id={fuoco.id}, Mana: {fuoco.costo_mana})\n")

    print("Assegnazione N:N tramite AbilitaAppresa:")
    print(
        f"- {link_aragorn.personaggio.nome} apprende {link_aragorn.abilita.nome_abilita} a livello {link_aragorn.livello_padronanza}"
    )
    print(
        f"- {link_merlino.personaggio.nome} apprende {link_merlino.abilita.nome_abilita} a livello {link_merlino.livello_padronanza}\n"
    )

    link_merlino.potenzia()
    print("Merlino si allena e potenzia l'abilita!")
    print(f"Nuovo livello padronanza Merlino: {link_merlino.livello_padronanza}")
    print(f"Livello padronanza Aragorn (inalterato): {link_aragorn.livello_padronanza}")


if __name__ == "__main__":
    main()
