# Esercizio 06: Centro sportivo

> **Obiettivo:** modellare otto entità/classi e vincoli che attraversano più relazioni.

## Il contesto

Un'organizzazione gestisce centri sportivi, identificati da codice e nome. Ogni campo ha un codice e un tipo e appartiene a un solo centro; un centro può avere più campi o nessuno.

I soci, identificati da numero e nome, prenotano i campi. Ogni prenotazione ha un codice, data e ora di inizio e fine, e riguarda un solo socio e un solo campo. Un socio o un campo possono non avere prenotazioni. Un campo non può avere prenotazioni con intervalli sovrapposti.

Il centro organizza corsi, identificati da codice e titolo. Ogni corso appartiene a un centro ed è affidato a un solo istruttore, identificato da matricola e nome. Centri e istruttori possono avere più corsi oppure nessuno.

Un socio può iscriversi a più corsi e un corso può avere più soci, ma entrambi possono esistere senza iscrizioni. Ogni iscrizione ha un identificativo e una data; un socio non può iscriversi due volte allo stesso corso.

Ogni corso può prevedere più lezioni oppure nessuna. Ogni lezione ha codice, data e ora, appartiene a un solo corso e si svolge in un solo campo. Un campo può ospitare più lezioni o nessuna. Il campo della lezione deve appartenere al centro che organizza il corso.

> **User story:** Come responsabile, voglio gestire campi, prenotazioni e corsi dei centri sportivi.

## Consegna

In `student.md` disegna i diagrammi **ER** e **UML delle classi** con otto entità/classi, attributi, identificatori, chiavi esterne e cardinalità o molteplicità. Esplicita i vincoli sulle sovrapposizioni e sull'appartenenza dei campi, distinguendoli dalle cardinalità. Non sono richiesti sequenza, codice o test.
