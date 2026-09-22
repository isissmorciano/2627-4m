from src.m04_persistenza_dati_json.es03.student import (
    Personaggio,
    Guerriero,
    Mago,
    salva_squadra,
    carica_squadra,
)


def test_persistenza_preserva_classi_esatte(tmp_path):
    file_path = str(tmp_path / "sq.json")
    squadra_in = [
        Guerriero(1, "Conan", forza=15),
        Mago(2, "Merlino", mana=30),
        Personaggio(3, "Popolano"),
    ]

    salva_squadra(squadra_in, file_path)
    squadra_out = carica_squadra(file_path)

    assert len(squadra_out) == 3
    assert isinstance(squadra_out[0], Guerriero)
    assert squadra_out[0].forza == 15
    assert "⚔️" in squadra_out[0].attacca()

    assert isinstance(squadra_out[1], Mago)
    assert squadra_out[1].mana == 30
    assert "✨" in squadra_out[1].attacca()

    assert type(squadra_out[2]) is Personaggio
