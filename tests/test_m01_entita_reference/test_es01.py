from src.m01_prima_entita_e_dataclass.es01.reference import Personaggio


def test_creazione_istanza_valori_default():
    eroe = Personaggio(1, "Aragorn")
    assert eroe.id == 1
    assert eroe.nome == "Aragorn"
    assert eroe.livello == 1
    assert eroe.punti_vita == 100


def test_creazione_istanza_livello_personalizzato():
    eroe = Personaggio(2, "Legolas", livello=5)
    assert eroe.id == 2
    assert eroe.nome == "Legolas"
    assert eroe.livello == 5
    assert eroe.punti_vita == 100


def test_metodo_presentati():
    eroe = Personaggio(10, "Gimli", livello=3)
    atteso = "Sono Gimli, eroe di livello 3 con 100 PV."
    assert eroe.presentati() == atteso


def test_metodo_dunder_str():
    eroe = Personaggio(7, "Boromir")
    atteso = "Personaggio #7: Boromir (PV: 100/100)"
    assert str(eroe) == atteso


def test_indipendenza_istanze():
    eroe1 = Personaggio(1, "Eroe 1")
    eroe2 = Personaggio(2, "Eroe 2")
    eroe1.punti_vita = 80
    assert eroe1.punti_vita == 80
    assert eroe2.punti_vita == 100
