from src.m01_prima_entita_e_dataclass.es07.student import BiciElettrica


def test_creazione_default():
    bici = BiciElettrica("B-100", "City")
    assert bici.codice_telaio == "B-100"
    assert bici.modello == "City"
    assert bici.batteria_percentuale == 100
    assert bici.is_noleggiata is False


def test_noleggio_valido_con_batteria_sufficiente():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=25)
    assert bici.inizia_noleggio() is True
    assert bici.is_noleggiata is True


def test_noleggio_limite_sotto_soglia_20():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=19)
    assert bici.inizia_noleggio() is False
    assert bici.is_noleggiata is False


def test_noleggio_soglia_esatta_20():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=20)
    assert bici.inizia_noleggio() is True
    assert bici.is_noleggiata is True


def test_rifiuto_noleggio_se_gia_in_uso():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=80, is_noleggiata=True)
    assert bici.inizia_noleggio() is False


def test_termina_noleggio_valido():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=50, is_noleggiata=True)
    assert bici.termina_noleggio(30) is True
    assert bici.is_noleggiata is False
    assert bici.batteria_percentuale == 20


def test_termina_noleggio_consumo_estremo_blocca_a_zero():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=30, is_noleggiata=True)
    assert bici.termina_noleggio(50) is True
    assert bici.batteria_percentuale == 0
    assert bici.is_noleggiata is False


def test_termina_noleggio_su_bici_non_noleggiata():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=50, is_noleggiata=False)
    assert bici.termina_noleggio(10) is False


def test_ricarica_con_tetto_massimo_100():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=80)
    bici.ricarica(50)
    assert bici.batteria_percentuale == 100


def test_ricarica_valore_negativo_ignorato():
    bici = BiciElettrica("B-100", "City", batteria_percentuale=50)
    bici.ricarica(-20)
    assert bici.batteria_percentuale == 50
