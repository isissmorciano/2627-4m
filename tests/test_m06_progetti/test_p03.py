from src.m06_progetti_sintesi_design_first.p03_flotta_veicoli.modello_student import (
    Autovettura,
    Furgone,
    Manutenzione,
)
from src.m06_progetti_sintesi_design_first.p03_flotta_veicoli.gestore_student import (
    salva_flotta,
    carica_flotta,
)


def test_canone_polimorfico_furgone():
    auto = Autovettura("AA111AA", "Fiat", 40.0)
    furgone = Furgone("BB222BB", "Iveco", 50.0, capacita_quintali=10)

    assert auto.calcola_canone_giornaliero() == 40.0
    assert furgone.calcola_canone_giornaliero() == 100.0  # 50 + (10 * 5)


def test_persistenza_flotta_polimorfica(tmp_path):
    path = str(tmp_path / "flotta.json")
    f = Furgone("BB222BB", "Iveco", 50.0, capacita_quintali=12)
    f.registra_manutenzione(Manutenzione(1, "2026-05-10", "Tagliando", 250.0))

    salva_flotta([f], path)
    caricati = carica_flotta(path)

    assert len(caricati) == 1
    assert isinstance(caricati[0], Furgone)
    assert caricati[0].calcola_canone_giornaliero() == 110.0
    assert len(caricati[0].manutenzioni) == 1