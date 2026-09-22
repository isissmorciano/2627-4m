from dataclasses import is_dataclass
from src.m01_prima_entita_e_dataclass.es02_student import Personaggio


def test_e_una_dataclass():
    assert is_dataclass(Personaggio), "La classe Personaggio deve essere decorata con @dataclass."


def test_valori_default_dataclass():
    eroe = Personaggio(id=1, nome="Aragorn")
    assert eroe.id == 1
    assert eroe.nome == "Aragorn"
    assert eroe.livello == 1
    assert eroe.punti_vita == 100


def test_uguaglianza_per_valore():
    p1 = Personaggio(1, "Aragorn", 1, 100)
    p2 = Personaggio(1, "Aragorn", 1, 100)
    p3 = Personaggio(2, "Legolas", 1, 100)

    # Nelle dataclass l'operatore == confronta i valori, non la memoria!
    assert p1 == p2
    assert p1 != p3


def test_metodo_presentati():
    eroe = Personaggio(5, "Gandalf", livello=10, punti_vita=120)
    assert eroe.presentati() == "Sono Gandalf, eroe di livello 10 con 120 PV."
