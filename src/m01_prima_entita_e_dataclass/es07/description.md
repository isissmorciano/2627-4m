# Esercizio 07: Pipeline Completa Singola Entità — Dal Requisito Grezzo ai Test

> **Prerequisiti teorici**: Modulo 01 (Tutti i capitoli) e Modulo 00 (User Stories e Criteri)  
> **Obiettivo**: Eseguire in totale autonomia l'intera catena di ingegneria del software su una singola entità: Requisiti grezzi $\\to$ User Story e Criteri $\\to$ Modellazione ER e UML $\\to$ Codice Python Dataclass $\\to$ Collaudo Pytest.

---

## 1. Il Testo dei Requisiti del Committente

Leggi attentamente il verbale informale raccolto durante l'incontro con una startup di mobilità urbana (*GreenRide*):

> *«Gestiamo una flotta di biciclette elettriche a noleggio per le strade della città. Ogni mezzo deve avere una targa o matricola univoca (es. 'BIKE-042') che lo identifichi senza ambiguità. Per ciascuna bici registriamo il modello commerciale (es. 'CityPro'), il livello di carica della batteria espresso in percentuale (da 0 a 100%) e se è attualmente noleggiata da un cliente oppure è libera per la strada.*  
> *Le regole del noleggio sono categoriche: un utente può sbloccare e iniziare una corsa solo se la bici non è già in uso e solo se la batteria ha almeno il 20% di carica residua. Sotto il 20% la bici è considerata scarica e il noleggio deve essere rifiutato per sicurezza.*  
> *Quando l'utente termina la corsa comunicando il consumo di batteria stimato dal tragitto, la bici deve tornare disponibile e la batteria deve scalare (senza mai andare sotto lo zero). Infine, i nostri operatori sul furgone possono ricaricare la batteria fino al 100% massimo.»*

---

## 2. Consegna dell'Esercizio

In questo esercizio lo **scaffolding è azzerato**: dovrai costruire ogni artefatto partendo dal testo sovrastante.

### Fase 1 e 2 — Analisi e Modellazione (`student.md`)
Apri `student.md` e compila:
1. **User Story:** Formula canonica *Come [Ruolo] voglio [Azione] per [Scopo]*.
2. **Criteri di Accettazione:** 4-5 condizioni oggettive e verificabili (regola del 20%, sblocco, rilascio e consumo, ricarica a 100%).
3. **Diagramma ER:** Entità `BICI_ELETTRICA` con Primary Key e tipi relazionali.
4. **Class Diagram UML:** Classe `BiciElettrica` con attributi tipizzati e metodi operativi (`inizia_noleggio`, `termina_noleggio`, `ricarica`).

### Fase 3 — Implementazione in Python (`student.py`)
1. Implementa la `@dataclass BiciElettrica`.
2. Implementa i metodi operativi garantendo la protezione rigorosa degli invarianti.
3. Nella funzione `main()`, simula un ciclo d'uso reale:
   - Creazione di una bici con carica iniziale 25%.
   - Inizio noleggio valido (25% >= 20%) -> sbloccata.
   - Termine noleggio con consumo del 15% -> batteria scende al 10%, bici rilasciata.
   - Tentativo di nuovo noleggio -> respinto perché batteria al 10% (< 20%).
   - Ricarica operatore del 50% -> batteria torna al 60%, bici nuovamente pronta al noleggio.

---

## 3. Esempio di Esecuzione del `main()`
```text
=== SIMULAZIONE BIKE SHARING GREENRIDE ===
Bici BIKE-042 (CityPro) | Batteria: 25% | Noleggiata: False

Richiesta sblocco corsa -> Esito: True
Stato: Noleggiata: True | Batteria: 25%

Termine corsa (consumo 15%) -> Esito: True
Stato: Noleggiata: False | Batteria residua: 10%

Tentativo nuovo noleggio -> Esito: False
Operazione rifiutata: batteria insufficiente (< 20%)!

Intervento operatore: ricarica +50%
Nuovo stato: Noleggiata: False | Batteria: 60% (Pronta per il noleggio)
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es07.py
```
