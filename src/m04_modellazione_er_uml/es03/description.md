# Esercizio 03: Corsi di formazione

> **Obiettivo:** modellare cinque entità/classi e una relazione molti-a-molti con dati propri.

## Il contesto

Un centro organizza corsi. Ogni corso ha un codice, un titolo, una data di inizio e un docente responsabile. I docenti sono identificati da una matricola e hanno nome e specializzazione; possono essere registrati anche senza corsi.

Ogni corso si tiene in una sola aula, identificata da codice, nome e capienza. Un'aula può ospitare più corsi nel tempo oppure nessuno.

Gli studenti, identificati da matricola e nome, possono iscriversi a più corsi. Anche un corso può avere più studenti, ma studenti e corsi possono esistere prima di qualsiasi iscrizione. Per ogni iscrizione si registrano un identificativo, la data e, soltanto dopo l'esame, un eventuale voto. Lo stesso studente non può iscriversi due volte allo stesso corso.

> **User story:** Come segreteria, voglio conoscere docenti, aule e iscritti di ogni corso e conservare l'esito di ciascuna iscrizione.

## Consegna

In `student.md` disegna i diagrammi **ER** e **UML delle classi** con cinque entità/classi, attributi, identificatori, chiavi esterne, cardinalità o molteplicità e dati facoltativi. Descrivi i vincoli non direttamente espressi e verifica che il voto appartenga alla singola iscrizione. Non sono richiesti sequenza, codice o test.
