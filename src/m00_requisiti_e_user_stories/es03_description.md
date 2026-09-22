# Esercizio 03: Criteri con Regole di Business ed Edge Cases

> **Prerequisiti teorici**: Modulo 00 (Cap. 03 - Dalle User Stories ai Requisiti)  
> **Obiettivo**: Imparare a individuare i casi limite (*edge cases*) e formalizzare le soglie numeriche all'interno dei Criteri di Accettazione.

---

## 1. Cosa sono i Casi Limite (Edge Cases)?

Nei sistemi reali il software fallisce quasi sempre sui **valori di confine**:
* Esattamente sulla soglia numerica (es. cosa succede a 15 posti precisi? Vale `< 15` o `<= 15`?).
* Sui valori estremi (zero, liste piene, valori massimi).
* Sulle azioni duplicate (provare a fare due volte la stessa operazione).

I Criteri di Accettazione devono specificare in modo inequivocabile come il sistema si comporta sia nei casi tipici, sia esattamente sui confini delle regole di business.

---

## 2. Lo Scenario di Business

Nel gestionale di un centro fitness abbiamo la seguente User Story:

> **User Story:**  
> *«Come Socio della palestra, voglio prenotare un posto per una sessione di allenamento a calendario, per assicurarmi la postazione nell'orario desiderato.»*

Il committente ci fornisce queste regole operative:
- La sala di allenamento ha una capienza massima fissa di 15 postazioni.
- Un socio può prenotare solo se ci sono posti disponibili.
- Quando viene prenotato il 15° posto, la sessione deve passare automaticamente allo stato "Esaurita" e rifiutare prenotazioni successive.
- Un socio non può prenotarsi due volte alla stessa sessione (blocco dei duplicati).
- Se la prenotazione va a buon fine, il sistema scala 1 ingresso dal carnet del socio e incrementa il contatore dei prenotati.
- Se la prenotazione viene rifiutata (posto esaurito o socio già iscritto), il carnet del socio non deve essere intaccato.

---

## 3. Consegna dell'Esercizio

Apri il file `es03_student.md` e compila i **Criteri di Accettazione (Definition of Done)** coprendo:
1. La condizione nominale di prenotazione con posti liberi.
2. Il caso limite esatto dell'ultimo posto disponibile (dal 14° al 15° posto).
3. Il caso limite di sessione al completo (tentativo di 16ª prenotazione).
4. La regola di business sul tentativo di prenotazione duplicata dallo stesso socio.
5. La protezione dell'invariante sul carnet ingressi in caso di operazione rifiutata.
