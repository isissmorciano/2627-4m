# Esercizio 01: C4 Model Livello 1 — System Context Base (Prenotazione Campi)

> **Prerequisiti teorici**: Modulo 00 (Cap. 02 - Visione di Sistema: Il C4 Model)  
> **Obiettivo**: Imparare a mappare il sistema software dal livello più alto di astrazione (*System Context*), identificando l'attore umano primario, il confine del sistema (scatola nera) e il servizio esterno integrato.

---

## 1. Cos'è il System Context (C4 Livello 1)?

Il diagramma di **System Context** risponde a due sole domande guardando il sistema "dallo spazio":
1. **Chi sono gli utenti umani** che usano il software?
2. **Con quali sistemi o servizi esterni/API** il software comunica per funzionare?

A questo livello non ci interessa se il codice è scritto in Python o quale database useremo: il nostro sistema al centro è rappresentato come una **scatola chiusa**.

---

## 2. Lo Scenario di Business

Un centro sportivo locale vuole automatizzare la prenotazione dei propri campi da paddle:

> **Capitolato del Committente:**  
> *«Vogliamo una piattaforma software ('PaddleHub') accessibile da smartphone e computer. I giocatori devono poter consultare la disponibilità degli orari, bloccare un campo ed effettuare il pagamento immediato con carta di credito. La gestione delle transazioni finanziarie non risiederà sui nostri server, ma sarà delegata interamente al gateway bancario esterno Stripe.»*

---

## 3. Consegna dell'Esercizio

Apri `student.md` e crea il diagramma Mermaid `flowchart LR`:
1. Definisci l'attore umano: `👤 Giocatore`.
2. Definisci il sistema centrale: `🏢 PaddleHub (Piattaforma Prenotazioni)`.
3. Definisci il servizio esterno: `💳 Stripe (Gateway Pagamenti)`.
4. Traccia le frecce direzionali inserendo etichette esplicative sulle interazioni.