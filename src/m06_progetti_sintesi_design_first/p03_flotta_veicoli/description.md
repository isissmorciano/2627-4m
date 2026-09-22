# Progetto 03: Gestione Flotta Logistica e Noleggio (Traccia Business B)

> **Obiettivo**: Modellare un sistema di noleggio veicoli che unisce Ereditarietà IS-A (`Furgone` / `Autovettura`), storico manutenzioni (1:N) e calcolo dinamico del canone con persistenza JSON.

---

## 1. Capitolato del Committente

> *«La nostra società di autonoleggio gestisce un parco mezzi. Tutti i veicoli hanno targa, marca, tariffa_giornaliera_base e stato_disponibile. I veicoli si dividono in Autovetture (con numero posti) e Furgoni (con capacita_carico_quintali).*  
> *Il canone di noleggio effettivo è polimorfico: le Autovetture applicano la tariffa base, mentre i Furgoni aggiungono un sovrapprezzo di 5.00€ per ogni quintale di carico utile.*  
> *Ogni veicolo mantiene un registro storico delle manutenzioni effettuate (1:N). Infine, il sistema deve salvare la flotta su file JSON e ricaricarla mantenendo le corrette sottoclassi.»*

---

## 2. Checklist di Consegna (5 Fasi)
- [ ] **Fase 1:** C4 L1/L2 + User Stories con Criteri di Accettazione.
- [ ] **Fase 2:** Diagramma ER con gerarchia veicoli e tabella `MANUTENZIONE` + Class Diagram UML.
- [ ] **Fase 3:** Diagramma di Sequenza del noleggio polimorfico.
- [ ] **Fase 4:** Codice Python Dataclass (`modello_student.py`) e persistenza JSON (`gestore_student.py`).
- [ ] **Fase 5:** Collaudo Pytest in `tests/test_m06_progetti/test_p03.py`.