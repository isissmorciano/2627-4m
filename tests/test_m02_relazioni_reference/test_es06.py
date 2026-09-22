from src.m02_relazioni_1_1_e_1_n.es06.reference import ClasseScolastica, Studente


def test_iscrizione_con_capienza():
    c = ClasseScolastica("4A", capienza_massima=2)
    assert c.iscrivi_studente(Studente(1, "A", 8.0)) is True
    assert c.iscrivi_studente(Studente(2, "B", 7.0)) is True
    assert c.iscrivi_studente(Studente(3, "C", 6.0)) is False


def test_calcolo_media_classe():
    c = ClasseScolastica("4A")
    assert c.calcola_media_classe() == 0.0
    c.iscrivi_studente(Studente(1, "A", 7.0))
    c.iscrivi_studente(Studente(2, "B", 8.0))
    assert c.calcola_media_classe() == 7.5


def test_elenco_promossi_include_soglia_esatta_6():
    c = ClasseScolastica("4A")
    c.iscrivi_studente(Studente(1, "A", 6.0))
    c.iscrivi_studente(Studente(2, "B", 5.9))
    c.iscrivi_studente(Studente(3, "C", 9.0))
    assert c.elenco_promossi() == ["A", "C"]
