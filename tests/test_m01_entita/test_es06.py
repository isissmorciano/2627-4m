from src.m01_prima_entita_e_dataclass.es06_student import ArticoloMagazzino


def test_creazione_articolo_default():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0)
    assert art.codice_sku == "SKU-01"
    assert art.nome == "Mouse"
    assert art.prezzo_unitario == 25.0
    assert art.quantita_disponibile == 0
    assert art.scorta_minima == 5


def test_scarico_valido():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0, quantita_disponibile=10)
    assert art.scarica(3) is True
    assert art.quantita_disponibile == 7


def test_scarico_eccessivo_respinto():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0, quantita_disponibile=4)
    assert art.scarica(5) is False
    assert art.quantita_disponibile == 4  # Giacenza non toccata


def test_scarico_quantita_non_valida():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0, quantita_disponibile=10)
    assert art.scarica(0) is False
    assert art.scarica(-3) is False
    assert art.quantita_disponibile == 10


def test_rifornimento_valido():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0, quantita_disponibile=5)
    assert art.rifornisci(15) is True
    assert art.quantita_disponibile == 20


def test_rifornimento_non_positivo_respinto():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0, quantita_disponibile=5)
    assert art.rifornisci(0) is False
    assert art.rifornisci(-5) is False
    assert art.quantita_disponibile == 5


def test_sotto_scorta_soglia_esatta():
    art = ArticoloMagazzino("SKU-01", "Mouse", 25.0, quantita_disponibile=6, scorta_minima=5)
    assert art.sotto_scorta() is False

    art.scarica(1)  # Ora quantita = 5 (uguale a scorta_minima)
    assert art.sotto_scorta() is True

    art.scarica(2)  # Ora quantita = 3 (< scorta_minima)
    assert art.sotto_scorta() is True


def test_valore_inventario():
    art = ArticoloMagazzino("SKU-01", "Monitor", 150.50, quantita_disponibile=4)
    assert art.valore_inventario() == 602.00
