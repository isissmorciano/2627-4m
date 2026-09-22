from src.m02_relazioni_1_1_e_1_n.es02.student import Paziente, CartellaClinica


def test_assegnazione_valida():
    p = Paziente("CF01", "Luca")
    c = CartellaClinica(1, "Controllo")
    assert p.assegna_cartella(c) is True
    assert p.cartella is c
    assert c.paziente is p


def test_rifiuto_doppia_assegnazione():
    p = Paziente("CF01", "Luca")
    c1 = CartellaClinica(1, "Controllo")
    c2 = CartellaClinica(2, "Visita")
    p.assegna_cartella(c1)
    assert p.assegna_cartella(c2) is False
    assert p.cartella is c1


def test_dimissione_azzera_reciprocamente():
    p = Paziente("CF01", "Luca")
    c = CartellaClinica(1, "Controllo")
    p.assegna_cartella(c)

    assert p.dimetti() is True
    assert p.cartella is None
    assert c.paziente is None


def test_dimissione_senza_cartella():
    p = Paziente("CF01", "Luca")
    assert p.dimetti() is False
