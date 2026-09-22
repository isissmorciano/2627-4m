from src.m02_relazioni_1_1_e_1_n.es04.reference import Personaggio, Inventario, Oggetto


def test_raccolta_senza_zaino_fallisce():
    eroe = Personaggio(1, "Conan")
    assert eroe.raccogli_oggetto(Oggetto(1, "Pozione", "Cura")) is False


def test_raccolta_con_delega_ha_successo():
    eroe = Personaggio(1, "Conan", inventario=Inventario(101, 5))
    assert eroe.raccogli_oggetto(Oggetto(1, "Pozione", "Cura")) is True
    assert len(eroe.inventario.oggetti) == 1


def test_usa_oggetto_rimuove_dallo_zaino():
    eroe = Personaggio(1, "Conan", inventario=Inventario(101, 5))
    eroe.raccogli_oggetto(Oggetto(1, "Pozione", "Cura"))
    assert eroe.usa_oggetto("Pozione") is True
    assert len(eroe.inventario.oggetti) == 0


def test_usa_oggetto_inesistente():
    eroe = Personaggio(1, "Conan", inventario=Inventario(101, 5))
    assert eroe.usa_oggetto("Pozione") is False
