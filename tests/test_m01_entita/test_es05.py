from src.m01_prima_entita_e_dataclass.es05.student import TesseraAbbonamento


def test_creazione_tessera_default():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri")
    assert tessera.codice_tessera == "CARD-101"
    assert tessera.titolare == "Paolo Neri"
    assert tessera.ingressi_residui == 10
    assert tessera.is_attiva is True


def test_accesso_valido_scala_un_ingresso():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri", ingressi_residui=5)
    esito = tessera.valida_accesso()
    assert esito is True
    assert tessera.ingressi_residui == 4
    assert tessera.is_attiva is True


def test_ultimo_ingresso_disattiva_tessera():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri", ingressi_residui=1)
    esito = tessera.valida_accesso()
    assert esito is True
    assert tessera.ingressi_residui == 0
    assert tessera.is_attiva is False


def test_accesso_negato_su_tessera_esaurita():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri", ingressi_residui=0, is_attiva=False)
    esito = tessera.valida_accesso()
    assert esito is False
    assert tessera.ingressi_residui == 0


def test_accesso_negato_su_tessera_bloccata_manualmente():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri", ingressi_residui=5)
    tessera.blocca_tessera()
    assert tessera.is_attiva is False
    assert tessera.valida_accesso() is False
    assert tessera.ingressi_residui == 5  # Nessun ingresso consumato


def test_ricarica_riattiva_tessera():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri", ingressi_residui=0, is_attiva=False)
    assert tessera.ricarica_ingressi(10) is True
    assert tessera.ingressi_residui == 10
    assert tessera.is_attiva is True


def test_ricarica_quantita_non_valida():
    tessera = TesseraAbbonamento("CARD-101", "Paolo Neri", ingressi_residui=2, is_attiva=True)
    assert tessera.ricarica_ingressi(0) is False
    assert tessera.ricarica_ingressi(-5) is False
    assert tessera.ingressi_residui == 2
