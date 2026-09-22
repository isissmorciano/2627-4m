from src.m03_relazioni_nn_ed_ereditarieta.es06_reference import CartaCredito, BonificoBancario


def test_carta_credito_plafond_sufficiente():
    c = CartaCredito("1111", 150.0)
    ok, msg = c.elabora(100.0)
    assert ok is True
    assert c.plafond_residuo == 50.0
    assert "approvato" in msg.lower()


def test_carta_credito_plafond_insufficiente():
    c = CartaCredito("1111", 50.0)
    ok, msg = c.elabora(100.0)
    assert ok is False
    assert c.plafond_residuo == 50.0
    assert "insufficiente" in msg.lower()


def test_bonifico_calcola_commissione():
    b = BonificoBancario("IT01", commissione_fissa=2.0)
    ok, msg = b.elabora(100.0)
    assert ok is True
    assert "102.00" in msg
    assert "IT01" in msg
