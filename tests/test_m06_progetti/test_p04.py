from src.m06_progetti_sintesi_design_first.p04_gestionale_corsi_palestra.modello_student import (
    Corso,
    Socio,
    Tessera,
)
from src.m06_progetti_sintesi_design_first.p04_gestionale_corsi_palestra.gestore_student import (
    salva_corso,
    carica_corso,
)


def test_iscrizione_con_tessera_valida():
    corso = Corso("YOGA-01", "Yoga Base", capienza_massima=10)
    socio = Socio("S01", "Elena", Tessera("T01", ingressi=5))

    assert corso.iscrivi_socio(1, socio, "2026-09-01") is True
    assert len(corso.iscrizioni) == 1
    assert socio.tessera.ingressi == 4


def test_iscrizione_fallisce_con_tessera_esaurita():
    corso = Corso("YOGA-01", "Yoga Base", capienza_massima=10)
    socio = Socio("S01", "Elena", Tessera("T01", ingressi=0, is_attiva=False))

    assert corso.iscrivi_socio(1, socio, "2026-09-01") is False
    assert len(corso.iscrizioni) == 0


def test_iscrizione_fallisce_se_corso_pieno():
    corso = Corso("YOGA-01", "Yoga Base", capienza_massima=1)
    s1 = Socio("S01", "Elena", Tessera("T01", ingressi=5))
    s2 = Socio("S02", "Marco", Tessera("T02", ingressi=5))

    assert corso.iscrivi_socio(1, s1, "2026-09-01") is True
    assert corso.iscrivi_socio(2, s2, "2026-09-01") is False
    assert s2.tessera.ingressi == 5  # Ingresso non consumato!


def test_roundtrip_persistenza_corso(tmp_path):
    path = str(tmp_path / "corso.json")
    corso = Corso("PIL-02", "Pilates", capienza_massima=5)
    socio = Socio("S10", "Anna", Tessera("T10", ingressi=3))
    corso.iscrivi_socio(1, socio, "2026-09-02")

    salva_corso(corso, path)
    ricaricato = carica_corso(path)

    assert ricaricato.codice == "PIL-02"
    assert len(ricaricato.iscrizioni) == 1
    assert ricaricato.iscrizioni[0].socio.nome == "Anna"
    assert ricaricato.iscrizioni[0].socio.tessera.ingressi == 2