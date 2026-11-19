# Esercizio 05: Festival musicale

> **Obiettivo:** modellare sette entità/classi e più relazioni intorno allo stesso evento.

## Il contesto

Un festival organizza concerti, ciascuno identificato da un codice e descritto da titolo, data e ora. Ogni concerto si svolge su un solo palco; un palco, identificato da codice, nome e capienza, può ospitare più concerti oppure nessuno.

Il festival registra gli artisti con codice e nome d'arte. Un artista può esibirsi in più concerti e ogni concerto può prevedere più artisti, o nessuno durante la preparazione. Per ogni ingaggio si registrano un identificativo e il ruolo dell'artista in quel concerto. Uno stesso artista non può avere due ingaggi per lo stesso concerto.

Gli spettatori sono identificati da codice e nome. Ciascun biglietto ha un numero, è intestato a un solo spettatore, riguarda un solo concerto e appartiene a una sola categoria. Le categorie hanno codice, nome e prezzo; possono esistere anche senza biglietti venduti. Uno spettatore e un concerto possono avere zero o più biglietti. I biglietti emessi per un concerto non devono superare la capienza del suo palco.

> **User story:** Come organizzatore, voglio programmare concerti, artisti e vendite senza superare la capienza.

## Consegna

In `student.md` realizza il modello **ER** e il diagramma delle classi **UML**, con sette entità/classi, attributi, identificatori, chiavi esterne e cardinalità o molteplicità. Spiega i vincoli non esprimibili con le sole relazioni e verifica che gli artisti possano essere programmati prima della vendita dei biglietti. Non sono richiesti sequenza, codice o test.
