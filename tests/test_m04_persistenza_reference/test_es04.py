from src.m04_persistenza_dati_json.es04.reference import (
    Utente,
    Tessera,
    salva_utente,
    carica_utente,
)


def test_roundtrip_con_vera_istanza_tessera(tmp_path):
    file_path = str(tmp_path / "u.json")
    u = Utente(1, "Mario", Tessera("T1", 8))

    salva_utente(u, file_path)
    caricato = carica_utente(file_path)

    assert isinstance(caricato, Utente)
    assert isinstance(caricato.tessera, Tessera)
    assert caricato.tessera.ingressi == 8

    assert caricato.tessera.valida() is True
    assert caricato.tessera.ingressi == 7


def test_roundtrip_utente_senza_tessera(tmp_path):
    file_path = str(tmp_path / "u_notessera.json")
    u = Utente(2, "Anna", None)

    salva_utente(u, file_path)
    caricato = carica_utente(file_path)

    assert caricato.tessera is None
