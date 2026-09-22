from src.m03_relazioni_nn_ed_ereditarieta.es02.reference import Personaggio, Abilita, AbilitaAppresa


def test_calcolo_potenza_effettiva():
    e = Personaggio(1, "Mago")
    a = Abilita(1, "Dardo", danno_base=15, costo_mana=10)
    link = AbilitaAppresa(1, e, a, livello_padronanza=4)
    assert link.calcola_potenza_effettiva() == 60


def test_messaggio_esegui_colpo():
    e = Personaggio(1, "Thor")
    a = Abilita(1, "Fulmine", danno_base=20, costo_mana=15)
    link = AbilitaAppresa(1, e, a, livello_padronanza=2)
    assert link.esegui_colpo() == "Thor usa Fulmine (Liv. 2) infliggendo 40 danni!"
