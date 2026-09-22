from src.m03_relazioni_nn_ed_ereditarieta.es01.student import Personaggio, Abilita, AbilitaAppresa


def test_creazione_legame_nn():
    e = Personaggio(1, "Eroe")
    a = Abilita(10, "Cura", 15)
    link = AbilitaAppresa(100, e, a)

    assert link.id == 100
    assert link.personaggio.nome == "Eroe"
    assert link.abilita.nome_abilita == "Cura"
    assert link.livello_padronanza == 1


def test_potenziamento_fino_a_massimo_5():
    e = Personaggio(1, "Eroe")
    a = Abilita(10, "Cura", 15)
    link = AbilitaAppresa(100, e, a, livello_padronanza=3)

    link.potenzia()
    assert link.livello_padronanza == 4
    link.potenzia()
    assert link.livello_padronanza == 5
    link.potenzia()
    assert link.livello_padronanza == 5  # Non deve superare 5


def test_indipendenza_livelli_stessa_abilita():
    e1 = Personaggio(1, "Eroe1")
    e2 = Personaggio(2, "Eroe2")
    fuoco = Abilita(10, "Fuoco", 20)

    l1 = AbilitaAppresa(1, e1, fuoco, 1)
    l2 = AbilitaAppresa(2, e2, fuoco, 4)

    l1.potenzia()
    assert l1.livello_padronanza == 2
    assert l2.livello_padronanza == 4
