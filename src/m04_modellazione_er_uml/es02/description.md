# Esercizio 02: Partite e convocazioni

> **Obiettivo:** modellare quattro entità/classi, compresi due ruoli della stessa entità.

## Il contesto

Un campionato registra le squadre tramite codice e nome. Ogni giocatore ha una matricola, un nome e appartiene a una sola squadra; una squadra può avere anche nessun giocatore.

Ogni partita ha un codice e una data e vede affrontarsi esattamente due squadre distinte: una in casa e una in trasferta. Una squadra può partecipare a molte partite oppure a nessuna.

Per ogni giocatore convocato in una partita si registra un codice di convocazione, il ruolo svolto e i minuti giocati. Un giocatore può essere convocato per più partite e una partita può avere più convocazioni, oppure nessuna finché non viene preparata. Un giocatore compare al massimo una volta nella stessa partita e può essere convocato solo se appartiene a una delle due squadre coinvolte.

> **User story:** Come organizzatore, voglio registrare le partite e i giocatori convocati per ciascuna, distinguendo squadra di casa e squadra ospite.

## Consegna

In `student.md` disegna i diagrammi **ER** e **UML delle classi** con quattro entità/classi, attributi, identificatori, chiavi esterne e cardinalità o molteplicità. Descrivi i vincoli non esprimibili direttamente nei diagrammi e verifica che sia possibile registrare squadre e partite senza convocazioni. Non sono richiesti sequenza, codice o test.
