# Esercizio 02: I Primi Criteri di Accettazione (Soluzione di Riferimento)

> **User Story di Riferimento:**  
> *«Come Lettore iscritto alla biblioteca, voglio prendere in prestito un libro presente a catalogo, per poterlo leggere a casa.»*

---

## Criteri di Accettazione (Definition of Done)

- [ ] La tessera del lettore deve essere attiva e non bloccata da sanzioni per ritardi pregressi.
- [ ] Il libro richiesto a catalogo deve avere almeno una copia disponibile (`copie_disponibili >= 1`).
- [ ] Se il prestito va a buon fine: il libro viene inserito tra i prestiti attivi del lettore, il contatore delle copie disponibili del libro diminuisce di 1 e viene fissata la data di restituzione a 30 giorni.
- [ ] Se non ci sono copie disponibili: la richiesta viene rifiutata, le copie rimangono a 0 e il sistema notifica che il libro è attualmente esaurito.
