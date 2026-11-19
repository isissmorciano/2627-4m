# Esercizio 04: Ordini online

> **Obiettivo:** modellare sei entità/classi, una relazione con dati propri e una relazione facoltativa uno-a-uno.

## Il contesto

Un negozio registra i clienti con codice, nome ed email. Un cliente può effettuare più ordini, oppure nessuno. Ogni ordine ha un numero, una data e appartiene a un solo cliente.

Il catalogo contiene articoli, ciascuno con codice, nome e prezzo attuale. Ogni ordine confermato comprende almeno una riga; ogni riga ha un identificativo, si riferisce a un solo articolo e conserva la quantità e il prezzo unitario applicato all'acquisto. Lo stesso articolo può comparire in molti ordini o in nessuno, ma al massimo una volta nello stesso ordine.

Un ordine può avere più pagamenti, anche nessuno: ognuno ha un identificativo, una data e un importo ed è riferito a un solo ordine. Quando viene spedito, all'ordine è associata una sola spedizione, con codice, data e indirizzo di consegna; prima della spedizione non ne ha alcuna. Ogni spedizione riguarda un solo ordine.

> **User story:** Come gestore, voglio conservare ordini, prezzi di acquisto, pagamenti e spedizioni dei clienti.

## Consegna

In `student.md` disegna i diagrammi **ER** e **UML delle classi** con sei entità/classi, attributi, identificatori, chiavi esterne e cardinalità o molteplicità. Spiega i vincoli aggiuntivi, la differenza tra prezzo attuale e prezzo acquistato e come garantire al massimo una spedizione per ordine. Non sono richiesti sequenza, codice o test.
