# Esercizio 05: Dominio Ticketing — Stato Booleano e Contatori a Scalare

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 e Cap. 03 - Dataclass, Metodi di stato e Booleani)  
> **Obiettivo**: Modellare e implementare un'entità per il controllo accessi (`TesseraAbbonamento`) con gestione combinata di un contatore a scalare (`ingressi_residui`) e di un flag di stato (`is_attiva: bool`).

---

## 1. Il Contesto di Business

Nei sistemi di controllo accessi (palestre, piscine, metropolitane, teatri), un titolo di viaggio o una tessera non memorizza solo dati anagrafici, ma governa una regola di sbarramento: **autorizzare o negare il passaggio al tornello**.

> **User Story:**  
> *«Come Titolare di una tessera a ingressi, voglio convalidare il mio accesso al tornello, per entrare nella struttura scalando un ingresso dal mio carnet fino a esaurimento.»*

### Criteri di Accettazione (Definition of Done)
- [ ] Ogni tessera è identificata univocamente da una Primary Key `codice_tessera` (stringa alfanumerica, es. `"CARD-1001"`).
- [ ] La tessera memorizza il nome del `titolare` (stringa), il numero di `ingressi_residui` (intero, default 10) e il flag `is_attiva` (booleano, default `True`).
- [ ] Il metodo `valida_accesso() -> bool`:
  - L'accesso è consentito **solo se** la tessera è attiva (`is_attiva == True`) **E** ci sono ingressi disponibili (`ingressi_residui > 0`).
  - In caso di successo: scala 1 ingresso (`ingressi_residui -= 1`).
  - Se dopo la convalida gli ingressi residui diventano pari a 0: la tessera viene disattivata automaticamente (`is_attiva = False`).
  - Restituisce `True` se l'accesso è concesso, `False` se negato (perché già disattiva o esaurita).
- [ ] Il metodo `ricarica_ingressi(quantita: int) -> bool`:
  - Se `quantita > 0`: aggiunge gli ingressi, riattiva la tessera (`is_attiva = True`) e restituisce `True`.
  - Se `quantita <= 0`: operazione non valida, lascia lo stato intatto e restituisce `False`.
- [ ] Il metodo `blocca_tessera() -> None`: disattiva la tessera impostando `is_attiva = False` (es. per smarrimento).

---

## 2. Consegna dell'Esercizio

### Parte 1 — Modellazione Statica (`es05_student.md`)
Disegna in Mermaid:
1. **Diagramma ER:** Entità `TESSERA_ABBONAMENTO` con `string codice_tessera PK`, `string titolare`, `int ingressi_residui`, `boolean is_attiva`.
2. **Class Diagram UML:** Classe `TesseraAbbonamento` con attributi tipizzati in Python e metodi `valida_accesso`, `ricarica_ingressi`, `blocca_tessera`.

### Parte 2 — Implementazione in Python (`es05_student.py`)
1. Implementa la classe con `@dataclass`.
2. Implementa i metodi operativi garantendo le transizioni di stato corrette.
3. Nella funzione `main()`:
   - Crea una tessera con 2 soli ingressi residui.
   - Convalida il primo ingresso: mostra esito `True` e ingressi rimasti (1).
   - Convalida il secondo ingresso: mostra esito `True`, ingressi rimasti (0) e disattivazione automatica della tessera (`is_attiva == False`).
   - Tenta un terzo accesso al tornello: dimostra che viene rifiutato (`False`).
   - Ricarica la tessera con 5 ingressi: dimostra che la tessera torna attiva (`True`) con 5 ingressi.

---

## 3. Esempio di Esecuzione del `main()`
```text
=== SIMULAZIONE CONTROLLO ACCESSI TORNELLO ===
Tessera CARD-555 (Titolare: Laura Verdi, Ingressi: 2, Attiva: True)

Convalida 1 -> Esito: True (Passaggio concesso)
Stato: 1 ingressi residui, Attiva: True

Convalida 2 -> Esito: True (Passaggio concesso)
Attenzione: ingressi esauriti, tessera disattivata!
Stato: 0 ingressi residui, Attiva: False

Convalida 3 -> Esito: False (Accesso negato al tornello!)
Stato: 0 ingressi residui, Attiva: False

Ricarica di 5 ingressi in cassa -> Esito: True
Stato: 5 ingressi residui, Attiva: True
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es05.py
```
