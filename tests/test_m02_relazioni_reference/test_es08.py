from src.m02_relazioni_1_1_e_1_n.es08.reference import Squadra, Giocatore


def test_liste_giocatori_indipendenti():
    s1 = Squadra("A")
    s2 = Squadra("B")
    s1.aggiungi_giocatore(Giocatore(10, "G1"))

    assert s1.conta_giocatori() == 1
    assert s2.conta_giocatori() == 0


def test_limite_massimo_11_giocatori():
    s = Squadra("A")
    for i in range(11):
        assert s.aggiungi_giocatore(Giocatore(i + 1, f"G{i + 1}")) is True
    assert s.aggiungi_giocatore(Giocatore(12, "G12")) is False
    assert s.conta_giocatori() == 11
