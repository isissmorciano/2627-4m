from src.m03_relazioni_nn_ed_ereditarieta.es05.reference import Personaggio, Guerriero, Mago


def test_attacco_guerriero_polimorfico():
    g = Guerriero(1, "Conan", forza=12)
    bersaglio = Personaggio(99, "Nemico", 100)
    msg = g.attacca(bersaglio)
    assert bersaglio.punti_vita == 78
    assert "⚔️" in msg


def test_attacco_mago_con_mana_sufficiente():
    m = Mago(2, "Merlino", mana=20)
    bersaglio = Personaggio(99, "Nemico", 100)
    msg = m.attacca(bersaglio)
    assert m.mana == 5
    assert bersaglio.punti_vita == 75
    assert "✨" in msg


def test_attacco_mago_senza_mana():
    m = Mago(2, "Merlino", mana=10)
    bersaglio = Personaggio(99, "Nemico", 100)
    m.attacca(bersaglio)
    assert m.mana == 10
    assert bersaglio.punti_vita == 100
