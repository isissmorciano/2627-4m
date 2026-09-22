# Esercizio 03: Criteri con Regole di Business ed Edge Cases

> **User Story di Riferimento:**  
> *«Come Socio della palestra, voglio prenotare un posto per una sessione di allenamento a calendario, per assicurarmi la postazione nell'orario desiderato.»*

---

## Criteri di Accettazione (Definition of Done)

<!-- 
Definisci i 5 criteri di accettazione richiesti, ponendo particolare attenzione 
ai casi limite (capienza massima 15, duplicati, carnet protetto).
Sostituisci i segnaposto [...] con le regole formali.
-->

- [ ] **Prenotazione con disponibilità:** Se i posti occupati sono [...] allora [...]
- [ ] **Caso limite ultimo posto (15/15):** Quando viene prenotato il 15° posto [...]
- [ ] **Caso limite capienza esaurita:** Se un socio tenta di prenotare con posti occupati >= 15 [...]
- [ ] **Regola anti-duplicato:** Se il socio risulta già presente nell'elenco iscritti [...]
- [ ] **Integrità del carnet:** In tutti i casi di prenotazione rifiutata [...]
