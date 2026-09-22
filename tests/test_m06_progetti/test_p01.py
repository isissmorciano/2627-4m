from src.m06_progetti_sintesi_design_first.p01_rpg_expansion.modello_student import (
    Personaggio,
    Ladro,
    Inventario,
    Oggetto,
    Missione,
    MissioneAccettata,
)
from src.m06_progetti_sintesi_design_first.p01_rpg_expansion.gestore_student import (
    salva_partita,
    carica_partita,
)


def test_attacco_furtivo_ladro():
    ladro = Ladro(1, "Garrett", destrezza=6)
    bersaglio = Personaggio(99, "Guardia", punti_vita=100)
    msg = ladro.attacca(bersaglio)

    assert bersaglio.punti_vita == 78  # 100 - (10 + 6*2 = 22)
    assert "🗡️" in msg


def test_completamento_missione_accredita_monete():
    eroe = Personaggio(1, "Robin", monete=10)
    quest = Missione(100, "Recupera amuleto", ricompensa_base=50)
    link = MissioneAccettata(1, eroe, quest)

    assert link.stato == "In Corso"
    link.completa_missione()
    assert link.stato == "Completata"
    assert eroe.monete == 60


def test_persistenza_completa_ladro(tmp_path):
    path = str(tmp_path / "partita_ladro.json")
    ladro = Ladro(1, "Garrett", destrezza=7, monete=100)
    ladro.inventario = Inventario(101, 5)
    ladro.inventario.aggiungi(Oggetto(1, "Pugnale", "Arma"))

    salva_partita(ladro, path)
    ricaricato = carica_partita(path)

    assert isinstance(ricaricato, Ladro)
    assert ricaricato.nome == "Garrett"
    assert ricaricato.destrezza == 7
    assert ricaricato.monete == 100
    assert len(ricaricato.inventario.oggetti) == 1
    assert ricaricato.inventario.oggetti[0].nome == "Pugnale"