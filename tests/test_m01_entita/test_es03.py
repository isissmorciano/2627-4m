from src.m01_prima_entita_e_dataclass.es03.student import Personaggio


def test_danno_parziale():
    eroe = Personaggio(1, "Conan", punti_vita=100, punti_vita_max=100)
    eroe.subisci_danno(35)
    assert eroe.punti_vita == 65
    assert eroe.is_vivo() is True


def test_danno_mortale_blocca_a_zero():
    eroe = Personaggio(1, "Conan", punti_vita=50, punti_vita_max=100)
    eroe.subisci_danno(80)
    assert eroe.punti_vita == 0
    assert eroe.is_vivo() is False


def test_danno_negativo_ignorato():
    eroe = Personaggio(1, "Conan", punti_vita=50, punti_vita_max=100)
    eroe.subisci_danno(-20)
    assert eroe.punti_vita == 50


def test_cura_parziale():
    eroe = Personaggio(1, "Conan", punti_vita=40, punti_vita_max=100)
    eroe.cura(30)
    assert eroe.punti_vita == 70


def test_cura_overflow_blocca_al_massimo():
    eroe = Personaggio(1, "Conan", punti_vita=80, punti_vita_max=100)
    eroe.cura(50)
    assert eroe.punti_vita == 100


def test_cura_negativa_ignorata():
    eroe = Personaggio(1, "Conan", punti_vita=80, punti_vita_max=100)
    eroe.cura(-10)
    assert eroe.punti_vita == 80
