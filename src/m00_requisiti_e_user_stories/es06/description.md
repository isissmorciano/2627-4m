# Esercizio 06: Detective dei Requisiti (Spec Review su Specifiche Difettose)

> **Prerequisiti teorici**: Modulo 00 (Cap. 03 - Dalle User Stories ai Requisiti) e Modulo 02 (Cap. 06 - Metodologia AI e Detective)  
> **Obiettivo**: Imparare a individuare ambiguità, buchi logici e criteri vaghi in specifiche scritte da terzi o generate da un'IA, correggendole prima di passare alla modellazione.

---

## 1. Il Ruolo del Detective dei Requisiti

In 3ª abbiamo imparato che il detective analizza il codice alla ricerca di bug prima di mandarlo in esecuzione.  
In 4ª il detective sale di livello: **analizza i requisiti prima che diventino codice**.

Un bug nei requisiti costa 10 volte meno se viene scovato sulla carta rispetto a quando è già stato programmato.

### 🔍 I 4 Difetti più Pericolosi da Stanare:
1. **Termini Vaghi / Non Misurabili:** Parole come *"veloce"*, *"spesa elevata"*, *"in modo intuitivo"*, *"un buon punteggio"*. Un computer capisce solo numeri, intervalli e booleani.
2. **Casi Limite Dimenticati:** Nessuna indicazione su cosa succede con valori pari a zero, elenchi vuoti o valori esattamente sulle soglie di confine.
3. **Assenza di Gestione del Rifiuto:** Specificare solo cosa accade quando l'azione riesce, dimenticando cosa fare in caso di fallimento o dati non validi.
4. **Ruoli Generici o Tautologie:** Ruoli come *"Utente generico"* o benefici che ripetono l'azione nel *per*.

---

## 2. Consegna dell'Esercizio

Apri il file `student.md`. Troverai **due specifiche difettose**:

### Caso A: La Specifica Vaga (Buono Sconto Fedeltà)
> *"Come utente del sito voglio applicare uno sconto fedeltà quando spendo abbastanza, per risparmiare dei soldi sul totale."*  
> **Criteri:**  
> - Si applica uno sconto sul carrello se la spesa è alta.  
> - Il sistema calcola il nuovo prezzo scontato.

### Caso B: La Specifica Incompleta (Ricarica Borsellino Elettronico)
> *"Come Studente della scuola, voglio ricaricare il credito del mio badge mensa online con carta di credito, per pagare i pasti senza usare contanti."*  
> **Criteri:**  
> - Lo studente inserisce la cifra desiderata e i dati della carta.  
> - Il saldo del badge viene incrementato dell'importo ricaricato.

Per ciascun caso dovrai:
1. Compilare il **Verdetto del Detective** elencando i buchi logici, le ambiguità e i rischi di implementazione.
2. Riscrivere la **User Story e i Criteri di Accettazione corretti e non ambigui**.
