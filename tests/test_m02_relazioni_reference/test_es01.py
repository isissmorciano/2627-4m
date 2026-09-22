from src.m02_relazioni_1_1_e_1_n.es01_reference import Personaggio, Inventario


def test_stato_iniziale_scollegato():
    eroe = Personaggio(1, "Aragorn")
    zaino = Inventario(101, 25)
    assert eroe.inventario is None
    assert zaino.proprietario is None


def test_collegamento_reciproco_1_a_1():
    eroe = Personaggio(1, "Aragorn")
    zaino = Inventario(101, 30)

    eroe.assegna_inventario(zaino)

    assert eroe.inventario is not None
    assert eroe.inventario.id == 101
    assert eroe.inventario.capacita_slot == 30

    assert zaino.proprietario is not None
    assert zaino.proprietario.id == 1
    assert zaino.proprietario.nome == "Aragorn"

    assert eroe.inventario is zaino
    assert zaino.proprietario is eroe
