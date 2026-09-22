# Progetto 04: Piattaforma Iscrizioni e Corsi Fitness (Traccia Business C)

> **Obiettivo**: Realizzare il sistema informativo per un centro fitness integrando Tessere (1:1), Corsi a numero chiuso (1:N) e Iscrizioni con capienza (N:N), salvataggio su file JSON e collaudo con Pytest.

---

## 1. Capitolato del Committente

> *«Il centro 'FitPro' gestisce Soci e Corsi (es. Pilates, Crossfit, Yoga). Ogni socio ha codice_socio, nome e una Tessera associata con ingressi residui.*  
> *Ogni Corso ha codice, titolo, capienza_massima e lista delle iscrizioni attive.*  
> *Uno studente può iscriversi a un corso solo se:*  
> *1. La sua tessera è attiva e ha almeno 1 ingresso disponibile.*  
> *2. Il corso non ha raggiunto la capienza massima.*  
> *Al momento dell'iscrizione, la capienza del corso viene impegnata e dalla tessera viene scalato 1 ingresso. Se il corso è pieno o gli ingressi sono esauriti, l'iscrizione è respinta.*  
> *I dati dei corsi e delle iscrizioni devono poter essere salvati su file JSON e ricaricati per visualizzare il report presenze.»*

---

## 2. Checklist di Consegna (5 Fasi)
- [ ] **Fase 1:** C4 Context e Container + User Stories con Criteri.
- [ ] **Fase 2:** Diagramma ER con `SOCIO`, `TESSERA`, `CORSO`, `ISCRIZIONE` + Class Diagram UML.
- [ ] **Fase 3:** Diagramma di Sequenza dell'iscrizione con verifica tessera e capienza.
- [ ] **Fase 4:** Codice Python Dataclass (`modello_student.py`) e persistenza JSON (`gestore_student.py`).
- [ ] **Fase 5:** Collaudo Pytest in `tests/test_m06_progetti/test_p04.py`.