from src.m04_persistenza_dati_json.es02.reference import (
    Inventario,
    Oggetto,
    salva_inventario,
    carica_inventario,
)


def test_ricostruzione_corretta_istanze_oggetti(tmp_path):
    file_path = str(tmp_path / "inv.json")
    inv = Inventario(1, 10)
    inv.oggetti.append(Oggetto(10, "Spada", "Arma"))
    inv.oggetti.append(Oggetto(20, "Scudo", "Armatura"))

    salva_inventario(inv, file_path)
    caricato = carica_inventario(file_path)

    assert isinstance(caricato, Inventario)
    assert len(caricato.oggetti) == 2
    for item in caricato.oggetti:
        assert isinstance(item, Oggetto)

    assert caricato.oggetti[0].nome == "Spada"
    assert caricato.oggetti[1].tipo == "Armatura"
