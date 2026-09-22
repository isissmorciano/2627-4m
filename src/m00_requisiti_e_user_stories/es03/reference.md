# Esercizio 03: Criteri con Regole di Business ed Edge Cases (Soluzione di Riferimento)

> **User Story di Riferimento:**  
> *«Come Socio della palestra, voglio prenotare un posto per una sessione di allenamento a calendario, per assicurarmi la postazione nell'orario desiderato.»*

---

## Criteri di Accettazione (Definition of Done)

- [ ] **Prenotazione con disponibilità:** Se i posti occupati sono < 15 e il socio non è già iscritto, la prenotazione viene confermata, il conteggio dei posti occupati aumenta di 1 e viene scalato 1 ingresso dal carnet del socio.
- [ ] **Caso limite ultimo posto (15/15):** Quando la prenotazione porta i posti occupati esattamente a 15, la sessione viene contrassegnata con lo stato "Esaurita".
- [ ] **Caso limite capienza esaurita:** Se un socio tenta di prenotare una sessione con posti occupati >= 15, la richiesta viene bloccata, il numero di prenotati resta 15 e viene restituito un messaggio di errore chiaro.
- [ ] **Regola anti-duplicato:** Se il socio risulta già iscritto alla medesima sessione, la richiesta viene respinta impedendo registrazioni multiple dello stesso utente.
- [ ] **Integrità del carnet:** In qualsiasi caso di prenotazione respinta (sessione piena o utente duplicato), il carnet del socio rimane inalterato (nessun credito scalato).
