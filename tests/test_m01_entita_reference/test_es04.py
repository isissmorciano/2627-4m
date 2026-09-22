from src.m01_prima_entita_e_dataclass.es04_reference import ContoCorrente


def test_creazione_conto_saldo_default():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi")
    assert conto.iban == "IT01A123"
    assert conto.titolare == "Anna Bianchi"
    assert conto.saldo == 0.0


def test_deposito_valido():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi")
    assert conto.deposita(150.50) is True
    assert conto.saldo == 150.50


def test_deposito_non_positivo_rifiutato():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi", saldo=100.0)
    assert conto.deposita(0.0) is False
    assert conto.deposita(-50.0) is False
    assert conto.saldo == 100.0


def test_prelievo_valido():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi", saldo=200.0)
    assert conto.preleva(80.0) is True
    assert conto.saldo == 120.0


def test_prelievo_scoperto_rifiutato():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi", saldo=50.0)
    assert conto.preleva(100.0) is False
    assert conto.saldo == 50.0  # Il saldo non deve essere toccato


def test_prelievo_importo_negativo():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi", saldo=50.0)
    assert conto.preleva(-20.0) is False
    assert conto.saldo == 50.0


def test_mostra_stato_formattato():
    conto = ContoCorrente(iban="IT01A123", titolare="Anna Bianchi", saldo=75.5)
    atteso = "Conto IT01A123 intestato a Anna Bianchi - Saldo: 75.50€"
    assert conto.mostra_stato() == atteso
