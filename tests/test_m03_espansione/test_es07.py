from src.m03_relazioni_nn_ed_ereditarieta.es07.student import Studente, Docente, Corso, iscrivi_studente_a_corso, Utente


def test_gerarchia_utenti():
    s = Studente(1, "A", "a@test.com", 50.0)
    d = Docente(2, "B", "b@test.com", 30.0)
    assert isinstance(s, Utente)
    assert isinstance(d, Utente)


def test_iscrizione_con_credito_sufficiente():
    s = Studente(1, "A", "a@test.com", 100.0)
    c = Corso("C1", "Titolo", 40.0)
    isc = iscrivi_studente_a_corso(1, s, c, "2026-01-01")

    assert isc is not None
    assert isc.stato == "Attivo"
    assert s.credito_disponibile == 60.0


def test_iscrizione_con_credito_insufficiente():
    s = Studente(1, "A", "a@test.com", 30.0)
    c = Corso("C1", "Titolo", 40.0)
    isc = iscrivi_studente_a_corso(1, s, c, "2026-01-01")

    assert isc is None
    assert s.credito_disponibile == 30.0
