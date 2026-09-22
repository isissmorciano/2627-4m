# Esercizio 02: I Primi Criteri di Accettazione (Definition of Done)

> **Prerequisiti teorici**: Modulo 00 (Cap. 03 - Dalle User Stories ai Requisiti)  
> **Obiettivo**: Imparare a corredare una User Story con Criteri di Accettazione chiari, misurabili e verificabili.

---

## 1. Perché servono i Criteri di Accettazione?

Una User Story da sola descrive l'intenzione, ma può rimanere vaga. Per renderla inequivocabile aggiungiamo sempre i **Criteri di Accettazione (Definition of Done)**: l'elenco delle condizioni che devono essere vere affinché la funzionalità sia considerata finita, corretta e collaudabile.

Un buon criterio di accettazione definisce:
* Le condizioni di partenza richieste.
* I vincoli numerici o di stato (es. capienza, limiti massimi).
* Il comportamento in caso di successo (cosa viene modificato o restituito).
* Il comportamento in caso di errore o rifiuto (cosa succede se il vincolo non è rispettato).

---

## 2. Lo Scenario di Business

Nel sistema informativo di una **Biblioteca Civica** abbiamo la seguente User Story:

> **User Story:**  
> *«Come Lettore iscritto alla biblioteca, voglio prendere in prestito un libro presente a catalogo, per poterlo leggere a casa.»*

---

## 3. Consegna dell'Esercizio

Apri il file `student.md` e definisci i **Criteri di Accettazione** per questa funzionalità.

Dovrai formalizzare 4 condizioni verificabili:
1. Requisito sullo stato della tessera del lettore.
2. Requisito sulla disponibilità di copie del libro.
3. Effetto del prestito andato a buon fine (aggiornamento copie e registrazione scadenza a 30 giorni).
4. Comportamento nel caso in cui tutte le copie siano già in prestito (copie disponibili = 0).
