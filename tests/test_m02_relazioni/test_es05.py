from src.m02_relazioni_1_1_e_1_n.es05.student import Carrello, ElementoCarrello


def test_calcolo_totale_carrello():
    c = Carrello(1)
    c.aggiungi_elemento(ElementoCarrello(1, "A", 2, 10.0))
    c.aggiungi_elemento(ElementoCarrello(2, "B", 1, 30.5))
    assert c.calcola_totale() == 50.5


def test_rimozione_prodotto_esistente():
    c = Carrello(1)
    c.aggiungi_elemento(ElementoCarrello(1, "A", 2, 10.0))
    assert c.rimuovi_prodotto(1) is True
    assert c.calcola_totale() == 0.0


def test_rimozione_prodotto_inesistente():
    c = Carrello(1)
    assert c.rimuovi_prodotto(999) is False
