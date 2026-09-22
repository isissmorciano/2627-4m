from src.m06_progetti_sintesi_design_first.p02_centro_sportivo.modello_reference import (
    Campo,
    Attrezzatura,
    Prenotazione,
)
from src.m06_progetti_sintesi_design_first.p02_centro_sportivo.gestore_reference import (
    salva_prenotazione,
    carica_prenotazione,
)


def test_calcolo_costo_totale_prenotazione():
    campo = Campo("PADDLE-1", "Paddle", 36.0)
    pren = Prenotazione(1, "Mario Rossi", campo, "2026-06-01 18:00")
    racchetta = Attrezzatura(10, "Racchetta", 3.0)
    palline = Attrezzatura(20, "Tubo Palline", 2.5)

    pren.aggiungi_noleggio(racchetta, 2)
    pren.aggiungi_noleggio(palline, 1)

    assert pren.calcola_costo_totale() == 44.50


def test_roundtrip_persistenza_prenotazione(tmp_path):
    path = str(tmp_path / "prenotazione.json")
    campo = Campo("TENNIS-1", "Tennis", 20.0)
    pren = Prenotazione(10, "Luca", campo, "2026-06-02 10:00")
    pren.aggiungi_noleggio(Attrezzatura(1, "Racchetta", 4.0), 1)

    salva_prenotazione(pren, path)
    ricaricata = carica_prenotazione(path)

    assert ricaricata.id_prenotazione == 10
    assert ricaricata.campo.codice_campo == "TENNIS-1"
    assert len(ricaricata.noleggi) == 1
    assert ricaricata.calcola_costo_totale() == 24.0