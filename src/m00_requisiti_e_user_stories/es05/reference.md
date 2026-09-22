# Esercizio 05: Scomposizione da Epic a User Stories Atomiche (Soluzione di Riferimento)

## US-01: Scrittura della Recensione (Cliente Acquirente)

**Come** Cliente che ha acquistato il prodotto  
**voglio** pubblicare una valutazione da 1 a 5 stelle con un commento di testo  
**per** condividere la mia esperienza d'uso con la community  

### Criteri di Accettazione (Definition of Done)
- [ ] Il voto deve essere un numero intero compreso rigorosamente tra 1 e 5 (estremi inclusi).
- [ ] Il commento di testo è facoltativo ma, se inserito, non può superare la lunghezza massima di 500 caratteri.
- [ ] La recensione inviata viene memorizzata inizialmente nello stato "In Attesa di Moderazione" e non è visibile al pubblico.

---

## US-02: Consultazione Recensioni e Media Voti (Visitatore)

**Come** Visitatore del catalogo online  
**voglio** visualizzare l'elenco delle recensioni approvate e il punteggio medio calcolato  
**per** valutare l'affidabilità e la qualità dell'articolo prima dell'acquisto  

### Criteri di Accettazione (Definition of Done)
- [ ] Nella scheda del prodotto vengono visualizzate solo le recensioni che hanno lo stato "Approvata".
- [ ] Il punteggio medio viene calcolato sommando i voti delle sole recensioni approvate e arrotondato a una cifra decimale.
- [ ] Se un prodotto non ha recensioni approvate, il sistema mostra la dicitura "Nessuna recensione disponibile" e la media non viene calcolata.

---

## US-03: Moderazione dei Feedback (Moderatore)

**Come** Moderatore della piattaforma  
**voglio** approvare o rifiutare le recensioni che si trovano in attesa di verifica  
**per** evitare che contenuti offensivi, falsi o spam compaiano pubblicamente sul catalogo  

### Criteri di Accettazione (Definition of Done)
- [ ] L'azione di moderazione è consentita solo a utenti autenticati con ruolo specifico di Moderatore.
- [ ] Una recensione rifiutata cambia stato in "Rifiutata", non viene mai mostrata pubblicamente e non contribuisce alla media voti del prodotto.
