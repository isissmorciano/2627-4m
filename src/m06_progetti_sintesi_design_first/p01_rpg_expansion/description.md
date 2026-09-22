# Progetto 01: Espansione del Motore RPG (Progetto Faro Guidato)

> **Obiettivo**: Estendere il motore di gioco di ruolo consolidando la pipeline completa in 5 fasi: C4 Model $\to$ User Stories $\to$ ER/UML $\to$ Sequenze $\to$ Dataclass Python + Persistenza JSON + Pytest.

---

## 1. Il Testo dei Requisiti del Committente

> *«La nostra software house vuole pubblicare la prima grande espansione del gioco 'Le Cronache di Pythonia'.*  
> *Dobbiamo introdurre tre novità fondamentali:*  
> *1. Una nuova classe specializzata di eroe: il **Ladro** (eredita da `Personaggio`), dotato di un attributo `destrezza: int`. Il suo attacco polimorfico infligge `10 + (destrezza * 2)` danni con un colpo furtivo alle spalle.*  
> *2. Il sistema delle **Missioni** (Quest): un eroe può intraprendere molte missioni e una missione può essere affrontata da molti eroi (relazione N:N). L'entità ponte `MissioneAccettata` deve memorizzare lo `stato` ('In Corso', 'Completata') e la `ricompensa_monete`.*  
> *3. Quando un eroe completa una missione (`completa_missione()`), lo stato passa a 'Completata' e il personaggio guadagna le monete.*  
> *4. Lo stato completo dell'eroe (compreso zaino, oggetti e missioni accettate) deve poter essere salvato su file JSON e ricaricato fedelmente al riavvio.»*

---

## 2. Checklist di Consegna (5 Fasi)
- [ ] **Fase 1:** C4 Context (L1) e Container (L2) + 3 User Stories con Criteri.
- [ ] **Fase 2:** Diagramma ER con tabella ponte `MISSIONE_ACCETTATA` + Class Diagram UML con classe `Ladro`.
- [ ] **Fase 3:** Diagrammi di Sequenza (Attacco Ladro e Completamento Missione).
- [ ] **Fase 4:** Implementazione `@dataclass` (`modello_student.py`) e modulo persistenza (`gestore_student.py`).
- [ ] **Fase 5:** Collaudo completo con `pytest tests/test_m06_progetti/test_p01.py`.