# Esercizio 04: Gestione del Rifiuto, Errori e Integrità dello Stato

> **User Story di Riferimento:**  
> *«Come Titolare di conto corrente, voglio prelevare contanti dallo sportello bancomat, per disporre di denaro liquido immediato.»*

---

## Criteri di Accettazione — Scenari di Rifiuto e Protezione Stato

<!-- 
Definisci le regole di business per ciascun caso di rifiuto.
Assicurati di specificare: condizione, blocco dell'azione, messaggio ed esito sullo stato del conto.
Sostituisci i segnaposto [...] con le regole formali.
-->

- [ ] **Rifiuto per PIN errato:** Se il codice PIN inserito non corrisponde [...]
- [ ] **Blocco di sicurezza tentativi PIN:** Al terzo tentativo consecutivo di PIN errato [...]
- [ ] **Rifiuto per saldo insufficiente:** Se l'importo richiesto supera il saldo disponibile [...]
- [ ] **Rifiuto per superamento limite giornaliero:** Se l'importo richiesto sommato ai prelievi odierni supera 500.00€ [...]
- [ ] **Guasto/Mancanza banconote ATM:** Se lo sportello non può erogare fisicamente le banconote [...]
