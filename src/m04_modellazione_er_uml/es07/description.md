# Esercizio 07: Ristorante

> **Obiettivo:** modellare nove entità/classi e collegare prenotazioni, servizio e pagamenti.

## Il contesto

Un ristorante ha sale, ciascuna con codice e nome, e tavoli, identificati da numero e numero di posti. Ogni tavolo si trova in una sola sala; una sala può avere più tavoli o nessuno.

I clienti, identificati da codice e nome, possono prenotare un tavolo. Ogni prenotazione ha un codice, data e ora di inizio e fine e numero di persone; è effettuata da un solo cliente per un solo tavolo. Clienti e tavoli possono non avere prenotazioni. Le prenotazioni dello stesso tavolo non possono sovrapporsi e il numero di persone non può superare i posti del tavolo.

Per una prenotazione può essere registrato al massimo un ordine; una prenotazione può anche non avere ancora un ordine. Ogni ordine ha un numero, è associato a una sola prenotazione ed è seguito da un solo cameriere. I camerieri hanno matricola e nome e possono seguire più ordini o nessuno.

Il menu contiene piatti con codice, nome e prezzo attuale. Un ordine contiene almeno una riga, con identificativo, quantità e prezzo unitario applicato; ogni riga riguarda un solo piatto. Un piatto può apparire in più ordini, ma al massimo una volta nello stesso ordine.

Un ordine può avere più pagamenti oppure nessuno. Ogni pagamento ha un codice, una data e un importo e si riferisce a un solo ordine.

> **User story:** Come responsabile, voglio gestire i tavoli e ricostruire ciò che è stato ordinato e pagato per ogni prenotazione.

## Consegna

In `student.md` disegna i diagrammi **ER** e **UML delle classi** con nove entità/classi, attributi, identificatori, chiavi esterne e cardinalità o molteplicità. Spiega come si rappresentano ordine facoltativo, storico dei prezzi e vincoli relativi ai tavoli. Non sono richiesti sequenza, codice o test.
