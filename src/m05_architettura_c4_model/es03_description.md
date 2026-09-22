# Esercizio 03: C4 Model Livello 2 — Container Monolite Classico (Registro Elettronico)

> **Prerequisiti teorici**: Modulo 00 (Cap. 02 - C4 Model Livello 2: Container)  
> **Obiettivo**: Aprire la scatola del sistema e identificare i confini software (Container) dell'architettura a tre blocchi classica: Frontend Web, Backend Python e Database Relazionale.

---

## 1. Cos'è un Container nel C4 Model?

Un **Container** nel C4 Model rappresenta una singola unità software eseguibile o un archivio dati separato:
* Un'interfaccia utente (es. Single Page App React/Vue o sito web).
* Un server applicativo o API Backend (il nostro programma Python).
* Una banca dati o file storage (Database PostgreSQL, SQLite, file JSON).

---

## 2. Lo Scenario di Business

Il Ministero dell'Istruzione commissiona il nuovo *Registro Elettronico Scolastico*:

> **Capitolato Tecnico:**  
> *«I docenti e le famiglie accedono al servizio tramite un portale Web fruibile da browser. Tutte le richieste (voti, assenze, note) vengono inviate tramite chiamate HTTPS a un'applicazione Backend sviluppata in Python. Questo server contiene tutta la logica di business, i vincoli di accesso e i calcoli delle medie. Infine, tutti i dati anagrafici e scolastici vengono salvati stabilmente in un Database Relazionale aziendale protetto.»*

---

## 3. Consegna dell'Esercizio

Apri `es03_student.md` e disegna il Container Diagram:
1. Attori: `Docente` e `Famiglia/Studente`.
2. Confine del sistema (Boundary): `Registro Scolastico`.
3. Container interni:
   - `Web App UI (HTML5 / JavaScript)`
   - `Backend API Server (Python)`
   - `Database Relazionale (SQL)`
4. Protocolli di comunicazione sulle frecce (es. `HTTPS/JSON`, `SQL query / TCP`).