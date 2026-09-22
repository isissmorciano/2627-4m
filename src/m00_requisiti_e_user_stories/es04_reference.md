# Esercizio 04: Gestione del Rifiuto, Errori e Integrità dello Stato (Soluzione di Riferimento)

> **User Story di Riferimento:**  
> *«Come Titolare di conto corrente, voglio prelevare contanti dallo sportello bancomat, per disporre di denaro liquido immediato.»*

---

## Criteri di Accettazione — Scenari di Rifiuto e Protezione Stato

- [ ] **Rifiuto per PIN errato:** Se il codice PIN inserito non corrisponde, l'operazione di prelievo viene immediatamente interrotta, nessun contante viene erogato e viene mostrato il messaggio "PIN non corretto. Riprova." incrementando il contatore dei tentativi falliti.
- [ ] **Blocco di sicurezza tentativi PIN:** Al terzo tentativo consecutivo di PIN errato, la carta bancomat viene trattenuta/bloccata dal terminale per motivi di sicurezza e la sessione viene terminata.
- [ ] **Rifiuto per saldo insufficiente:** Se l'importo richiesto è superiore al saldo disponibile sul conto, l'operazione viene respinta con il messaggio "Fondi insufficienti", nessun contante viene erogato e il saldo del conto rimane rigorosamente inalterato (nessun addebito).
- [ ] **Rifiuto per superamento limite giornaliero:** Se l'importo richiesto (sommato ai prelievi già effettuati nella giornata) supera il tetto massimo di 500.00€, l'erogazione viene rifiutata con il messaggio "Limite giornaliero di 500€ superato" senza alterare il saldo.
- [ ] **Guasto/Mancanza banconote ATM:** Se lo sportello non dispone delle banconote fisiche necessarie, l'operazione viene annullata con il messaggio "Sportello temporaneamente non disponibile per l'importo richiesto", la carta viene restituita e non viene applicato alcun addebito sul conto.
