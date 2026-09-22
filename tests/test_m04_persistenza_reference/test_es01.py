from src.m04_persistenza_dati_json.es01.reference import (
    Personaggio,
    salva_personaggio,
    carica_personaggio,
)


def test_salva_e_carica_singolo_personaggio(tmp_path):
    file_test = str(tmp_path / "eroe_test.json")
    originale = Personaggio(10, "Gimli", livello=4, punti_vita=75)

    salva_personaggio(originale, file_test)
    ricaricato = carica_personaggio(file_test)

    assert isinstance(ricaricato, Personaggio)
    assert ricaricato.id == 10
    assert ricaricato.nome == "Gimli"
    assert ricaricato.livello == 4
    assert ricaricato.punti_vita == 75

    ricaricato.subisci_danno(25)
    assert ricaricato.punti_vita == 50
