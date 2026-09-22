from src.m03_relazioni_nn_ed_ereditarieta.es08.student import Veicolo, Furgone, Motore


def test_furgone_usa_super_e_ha_motore():
    m = Motore(2000, "Diesel")
    f = Furgone("AA000BB", "Ford", 90.0, 1200, motore=m)

    assert isinstance(f, Veicolo)
    assert f.targa == "AA000BB"
    assert f.marca == "Ford"
    assert f.tariffa_base == 90.0
    assert f.capacita_carico_kg == 1200
    assert f.motore is m
    assert f.motore.tipo_carburante == "Diesel"
