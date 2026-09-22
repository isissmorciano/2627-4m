# Esercizio 08: Detective delle Relazioni — Bug della Lista Condivisa e Violazione della Delega

> **Prerequisiti teorici**: Modulo 02 (Tutti i capitoli)  
> **Obiettivo**: Esercitare la revisione del codice scovando due dei bug più gravi e diffusi nelle relazioni 1:N in Python: il default mutabile condiviso tra istanze (`oggetti: list = []`) e la violazione dell'incapsulamento per mancata delega.

---

## 1. Lo Scenario del Detective

Un programmatore ha scritto una classe `Squadra` che contiene una lista di `Giocatore`.  
Il codice sembra funzionare a prima vista, ma nasconde due difetti letali:
1. **La trappola della lista condivisa:** ha dichiarato `giocatori: list[Giocatore] = []` anziché usare `field(default_factory=list)`. Di conseguenza, tutti gli oggetti `Squadra` del programma condividono la stessa lista in memoria RAM! Aggiungendo un giocatore alla Squadra A, compare magicamente anche nella Squadra B!
2. **Violazione dell'incapsulamento / Mancanza di delega:** il codice esterno accede direttamente con `squadra.giocatori.append(g)` invece di passare per un metodo protetto `aggiungi_giocatore(g)`.

---

## 2. Consegna dell'Esercizio

Apri `student.md` ed `student.py`:
1. Compila il **Verdetto del Detective** spiegando i due difetti.
2. Correggi il codice Python usando `field(default_factory=list)` e incapsulando l'aggiunta con limite massimo di 11 giocatori.
3. Dimostra nel `main()` che due squadre distinte rimangono rigorosamente indipendenti.

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es08.py
```
