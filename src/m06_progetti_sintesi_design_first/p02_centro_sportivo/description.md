# Progetto 02: Gestione Centro Sportivo e Noleggio (Traccia Business A)

> **Obiettivo**: Sviluppare da zero la piattaforma per un centro sportivo che gestisce la prenotazione dei campi (1:1), il calendario giornaliero (1:N) e il noleggio delle attrezzature (N:N con quantitativo e tariffa oraria).

---

## 1. Capitolato del Committente

> *«Il Centro Sportivo 'SportVillage' dispone di campi da gioco (Paddle, Tennis, Calcetto). Ogni campo ha un codice identificativo, la tipologia di sport e la tariffa oraria. I tesserati prenotano slot orari di gioco da 1 ora. Durante la prenotazione, possono noleggiare dell'attrezzatura (es. 2 racchette, 3 tubi di palline). Il sistema deve calcolare l'importo totale della seduta sommando il costo del campo e il costo orario delle attrezzature noleggiate moltiplicato per la quantità. Infine, il centro deve poter salvare le prenotazioni su file JSON e ricaricarle per stampare il riepilogo giornaliero degli incassi.»*

---

## 2. Checklist di Consegna (5 Fasi)
- [ ] **Fase 1:** C4 L1 (System Context) e L2 (Container) + 3 User Stories con Criteri.
- [ ] **Fase 2:** Diagramma ER con `CAMPO`, `PRENOTAZIONE`, `ATTREZZATURA`, `NOLEGGIO_ATTREZZATURA` + Class Diagram UML.
- [ ] **Fase 3:** Diagramma di Sequenza per il calcolo del costo totale della prenotazione.
- [ ] **Fase 4:** Codice Python Dataclass (`modello_student.py`) e modulo persistenza (`gestore_student.py`).
- [ ] **Fase 5:** Collaudo Pytest in `tests/test_m06_progetti/test_p02.py`.