from src.m03_relazioni_nn_ed_ereditarieta.es03.reference import Studente, Corso, Iscrizione


def test_verbalizzazione_valida():
    s = Studente(1, "A")
    c = Corso("C1", "Basi", 6)
    isc = Iscrizione(1, s, c, "2026-01-10")

    assert isc.is_superato() is False
    assert isc.verbalizza_voto(25) is True
    assert isc.voto_esame == 25
    assert isc.is_superato() is True


def test_verbalizzazione_fuori_scala_respinta():
    s = Studente(1, "A")
    c = Corso("C1", "Basi", 6)
    isc = Iscrizione(1, s, c, "2026-01-10")

    assert isc.verbalizza_voto(17) is False
    assert isc.verbalizza_voto(31) is False
    assert isc.voto_esame is None
    assert isc.is_superato() is False
