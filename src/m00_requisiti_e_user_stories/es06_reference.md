# Esercizio 06: Detective dei Requisiti (Soluzione di Riferimento)

## Caso A: La Specifica Vaga (Buono Sconto Fedeltà)

### 1. Verdetto del Detective
- **Ruolo generico:** "Utente del sito" è vago; la funzionalità riguarda solo i clienti registrati al programma fedeltà.
- **Termine non misurabile ("spesa abbastanza / alta"):** Non è specificata la soglia minima di spesa in Euro per aver diritto allo sconto.
- **Sconto non quantificato:** Non è indicata né la percentuale né l'importo fisso dello sconto applicato.
- **Casi limite assenti:** Non è specificato se lo sconto è cumulabile e se può rendere il totale negativo.

### 2. Specifiche Corrette
**Come** Cliente iscritto al Programma Fedeltà  
**voglio** applicare il mio coupon sconto del 15% al carrello  
**per** ridurre la spesa complessiva sui miei acquisti idonei  

#### Criteri di Accettazione (Definition of Done)
- [ ] Il coupon sconto del 15% è applicabile solo se il totale parziale degli articoli nel carrello è >= 40.00€.
- [ ] Se il totale è < 40.00€, il coupon viene respinto con il messaggio: "Spesa minima di 40€ non raggiunta".
- [ ] Il coupon non è applicabile su articoli già in saldo o promozione.
- [ ] Il calcolo dello sconto riduce il totale del carrello garantendo che l'importo da pagare non sia mai inferiore a 0.00€.

---

## Caso B: La Specifica Incompleta (Ricarica Borsellino Elettronico)

### 1. Verdetto del Detective
- **Assenza di vincoli sull'importo:** Non sono definiti né un taglio minimo né un massimale di ricarica (rischio di importi negativi o assurdi).
- **Assenza di gestione errori di pagamento:** Non è specificato cosa succede se la transazione bancaria viene negata dalla carta di credito.
- **Integrità dello stato non garantita:** Non è esplicitato che il saldo del badge NON deve essere incrementato se il pagamento non è andato a buon fine.

### 2. Specifiche Corrette
**Come** Studente (o genitore) titolare di un badge mensa scolastico  
**voglio** ricaricare il credito del badge tramite carta di pagamento  
**per** garantire la disponibilità dei fondi necessari al consumo dei pasti  

#### Criteri di Accettazione (Definition of Done)
- [ ] L'importo di ricarica selezionato deve essere compreso tra una soglia minima di 10.00€ e un massimale di 150.00€ per singola operazione.
- [ ] Se la transazione con la carta di credito ha successo: il saldo del badge viene incrementato esattamente della cifra ricaricata e viene generata una ricevuta digitale con ID transazione.
- [ ] Se la transazione viene rifiutata dalla banca: la ricarica viene annullata, il saldo del badge rimane intatto (nessun incremento) e viene mostrato il messaggio: "Pagamento non autorizzato dall'istituto bancario".
