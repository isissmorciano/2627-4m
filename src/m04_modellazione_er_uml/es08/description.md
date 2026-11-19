# Esercizio 08: Gilde e missioni

> **Obiettivo:** modellare dieci entità/classi, combinando più relazioni e vincoli temporali.

## Il contesto

Un gioco registra personaggi con identificativo, nome e livello. Ogni personaggio può avere al massimo un inventario, identificato da codice e capacità in slot; ogni inventario appartiene a un solo personaggio. Un oggetto ha identificativo, nome e tipo e può trovarsi in un solo inventario oppure nel mondo, senza inventario. Un inventario può contenere più oggetti o nessuno, senza superare la sua capacità.

Le abilità hanno identificativo, nome e costo in mana. Un personaggio può apprendere più abilità e un'abilità può essere appresa da più personaggi; entrambi possono esistere senza legami. Ogni abilità appresa ha un identificativo e un livello di padronanza da 1 a 5. Un personaggio non può apprendere due volte la stessa abilità.

Le missioni hanno codice e titolo. I personaggi possono partecipare a più missioni e ogni missione può avere più partecipanti, o nessuno prima di essere assegnata. Ogni partecipazione ha identificativo, data e ruolo; un personaggio può partecipare una sola volta alla stessa missione. Una partecipazione può ottenere più ricompense oppure nessuna; ogni ricompensa ha codice, descrizione e quantità e appartiene a una sola partecipazione.

Le gilde hanno codice e nome. Un personaggio può appartenere a gilde diverse nel tempo. Ogni iscrizione a una gilda ha un identificativo, una data di ingresso e, quando termina, una data di uscita. Le iscrizioni concluse rimangono nello storico. Ogni iscrizione riguarda una sola gilda e un solo personaggio; entrambi possono esistere senza iscrizioni. Un personaggio può avere al massimo un'iscrizione senza data di uscita.

> **User story:** Come giocatore, voglio gestire l'equipaggiamento e le abilità del mio personaggio e conservarne lo storico di missioni e gilde.

## Consegna

In `student.md` disegna i diagrammi **ER** e **UML delle classi** con dieci entità/classi, attributi, identificatori, chiavi esterne, cardinalità o molteplicità e dati facoltativi. Descrivi separatamente i vincoli su capacità, padronanza, coppie univoche e iscrizione attiva. Verifica che il personaggio possa cambiare gilda conservando lo storico. Non sono richiesti sequenza, codice o test.
