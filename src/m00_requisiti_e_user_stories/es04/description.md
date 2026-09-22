# Esercizio 04: Gestione del Rifiuto, Errori e Integrità dello Stato

> **Prerequisiti teorici**: Modulo 00 (Cap. 03 - Dalle User Stories ai Requisiti)  
> **Obiettivo**: Imparare a specificare nei Criteri di Accettazione cosa deve accadere quando un'operazione fallisce, garantendo messaggi chiari e l'integrità assoluta dello stato del sistema.

---

## 1. Perché specificare i casi di fallimento?

Nel software reale la maggior parte dei bug critici non riguarda il flusso nominale (*Happy Path*), ma la **gestione degli errori**.

Se un Criterio di Accettazione non specifica come gestire un rifiuto, il programmatore potrebbe:
* Lasciare che il programma vada in crash improvviso.
* Mostrare messaggi criptici o fuorvianti all'utente.
* **Corrompere i dati:** ad esempio scalare i soldi dal conto anche se lo sportello non è riuscito a erogare le banconote!

I Criteri di Accettazione devono stabilire tre certezze per ciascun caso di errore:
1. **La causa scatenante:** Quale condizione o vincolo è stato violato.
2. **L'integrità dello stato:** Confermare esplicitamente che nessuna variabile o saldo viene alterato parzialmente.
3. **Il feedback all'utente:** Il messaggio di errore esatto da restituire.

---

## 2. Lo Scenario di Business

Nel sistema software di uno sportello bancario automatico (ATM) abbiamo la seguente User Story:

> **User Story:**  
> *«Come Titolare di conto corrente, voglio prelevare contanti dallo sportello bancomat, per disporre di denaro liquido immediato.»*

Il committente specifica che il prelievo può fallire per diverse ragioni di sicurezza e conformità:
- Il PIN inserito non corrisponde a quello associato alla carta.
- Il saldo disponibile sul conto è inferiore all'importo richiesto (non è concesso alcun fido/scoperto).
- La cifra richiesta supera il limite massimo giornaliero di prelievo fissato a 500.00€.
- Il distributore fisico dell'ATM non dispone di banconote sufficienti per coprire la cifra.

---

## 3. Consegna dell'Esercizio

Apri il file `student.md` e compila i **Criteri di Accettazione (Definition of Done)** dedicati alla gestione degli errori e del rifiuto, formalizzando le 4 casistiche descritte e garantendo la protezione dello stato del conto.
