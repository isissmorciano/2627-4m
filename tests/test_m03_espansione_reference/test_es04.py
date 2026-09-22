from src.m03_relazioni_nn_ed_ereditarieta.es04.reference import Personaggio, Guerriero, Mago


def test_guerriero_eredita_da_personaggio():
    g = Guerriero(1, "Conan", forza=10)
    assert isinstance(g, Guerriero)
    assert isinstance(g, Personaggio)
    assert g.id == 1
    assert g.nome == "Conan"
    assert g.punti_vita == 120
    assert g.forza == 10


def test_mago_eredita_da_personaggio():
    m = Mago(2, "Merlino", mana=40)
    assert isinstance(m, Mago)
    assert isinstance(m, Personaggio)
    assert m.id == 2
    assert m.nome == "Merlino"
    assert m.punti_vita == 80
    assert m.mana == 40
