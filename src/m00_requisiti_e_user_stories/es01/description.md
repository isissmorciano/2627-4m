# Esercizio 01: La Formula Base della User Story (Chi / Cosa / Perché)

> **Prerequisiti teorici**: Modulo 00 (Cap. 03 - Dalle User Stories ai Requisiti)  
> **Obiettivo**: Imparare a formulare una User Story corretta dal punto di vista del vero utilizzatore finale, evitando gli anti-pattern tecnici e le tautologie.

---

## 1. La Formula Canonica

Una User Story descrive una funzionalità dal punto di vista di chi ne trae valore:

$$\textbf{Come } [\text{Ruolo/Attore}] \quad \textbf{voglio } [\text{Azione/Capacità}] \quad \textbf{per } [\text{Beneficio/Scopo}]$$

### ⚠️ I Due Errori più Comuni da Evitare:
1. **L'Anti-pattern Tecnico:** Scrivere storie dal punto di vista dello sviluppatore.  
   ❌ *«Come sviluppatore voglio creare la tabella `wishlist` nel database per salvare gli ID dei prodotti.»*  
   *Perché è sbagliato?* Il cliente o l'utente finale non sa cosa sia una tabella SQL; la funzionalità esiste per l'utente, non per il programmatore.
2. **Il Beneficio Tautologico:** Ripetere l'azione al posto del vero beneficio.  
   ❌ *«Come cliente voglio aggiungere un prodotto alla wishlist per... averlo nella wishlist.»*  
   *Perché è sbagliato?* Non spiega il *perché* di business (es. poterlo comprare in seguito, monitorarne il prezzo, non dimenticarsene).

---

## 2. Consegna dell'Esercizio

Apri il file `student.md` e completa i due task richiesti:

### Task A — Correzione dell'Anti-Pattern Tecnico
Ti viene fornita una User Story scritta male da un programmatore alle prime armi:
> *"Come programmatore Python voglio scrivere una funzione che salvi i preferiti su file JSON affinché i dati non vadano persi al riavvio."*

Riscrivila adottando il punto di vista del vero **Cliente/Utente** di un negozio online di fumetti e videogiochi, indicando chiaramente il beneficio reale di business.

### Task B — Dalla Richiesta Informale alla User Story
Leggi attentamente questa richiesta raccolta durante un'intervista con un committente:
> *"I nostri lettori spesso leggono capitoli lunghi dei webcomic sul nostro portale. Ci hanno segnalato che quando chiudono il browser o cambiano dispositivo perdono il segno e devono scorrere decine di pagine per ritrovare dove erano arrivati. Vorremmo dare la possibilità di inserire un segnalibro automatico o manuale sull'ultima tavola letta."*

Estrai e formalizza la User Story canonica:
- **Come:** identifica l'attore corretto.
- **Voglio:** definisci l'azione specifica desiderata.
- **per:** esplicita il beneficio concreto che risolve il problema descritto.
