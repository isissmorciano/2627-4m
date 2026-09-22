from src.m02_relazioni_1_1_e_1_n.es03_student import Inventario, Oggetto


def test_lista_oggetti_indipendente_tra_istanze():
    z1 = Inventario(1, 5)
    z2 = Inventario(2, 5)
    z1.aggiungi_oggetto(Oggetto(1, "A", "T"))
    assert z1.conta_oggetti() == 1
    assert z2.conta_oggetti() == 0  # Non devono condividere la lista!


def test_aggiunta_fino_a_capienza():
    z = Inventario(1, 2)
    assert z.aggiungi_oggetto(Oggetto(1, "A", "T")) is True
    assert z.aggiungi_oggetto(Oggetto(2, "B", "T")) is True
    assert z.aggiungi_oggetto(Oggetto(3, "C", "T")) is False
    assert z.conta_oggetti() == 2
