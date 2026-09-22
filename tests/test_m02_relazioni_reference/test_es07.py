from src.m02_relazioni_1_1_e_1_n.es07_reference import Hotel, Stanza


def test_prenotazione_camera_disponibile():
    h = Hotel("H")
    h.aggiungi_stanza(Stanza(101, "Doppia", 100.0))
    s = h.prenota_camera("Doppia")
    assert s is not None
    assert s.numero == 101
    assert s.is_occupata is True
    assert h.conta_camere_libere() == 0


def test_prenotazione_tipologia_esaurita():
    h = Hotel("H")
    h.aggiungi_stanza(Stanza(101, "Singola", 60.0))
    assert h.prenota_camera("Doppia") is None


def test_incasso_massimo():
    h = Hotel("H")
    h.aggiungi_stanza(Stanza(101, "Singola", 60.0))
    h.aggiungi_stanza(Stanza(102, "Doppia", 90.0))
    assert h.incasso_massimo_giornaliero() == 150.0
