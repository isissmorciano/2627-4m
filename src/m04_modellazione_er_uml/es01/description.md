# Esercizio 01: Prestiti in biblioteca

> **Obiettivo:** ricavare dal testo un modello ER e un diagramma delle classi UML con tre entità/classi.

## Il contesto

Una piccola biblioteca vuole tenere traccia delle copie dei libri e dei prestiti ai propri iscritti.

Per ogni iscritto registra un numero di tessera univoco, il nome e il cognome. Una persona può essere iscritta anche se non ha mai preso libri in prestito.

Ogni copia fisica ha un codice univoco, un titolo e il nome dell'autore. La biblioteca può possedere più copie dello stesso titolo, ciascuna con il proprio codice. Una copia può non essere mai stata prestata.

Quando un iscritto prende una copia in prestito, la biblioteca registra un numero identificativo del prestito, la data di inizio e la data di scadenza prevista. Alla restituzione registra anche la data effettiva di restituzione, che prima di quel momento non è presente. Ogni prestito riguarda una sola copia ed è effettuato da un solo iscritto.

Un iscritto può avere più prestiti, anche contemporaneamente. Una copia può essere prestata più volte nel tempo, ma non può avere più di un prestito non ancora restituito nello stesso momento. I prestiti conclusi rimangono nello storico.

> **User story:** Come bibliotecario, voglio registrare i prestiti e le restituzioni, per sapere quali copie sono disponibili e consultare lo storico dei prestiti.

## Consegna

1. Individua **tre entità**, i loro attributi e gli identificatori. In questo esercizio il titolo e il nome dell'autore sono dati della copia: non creare entità separate per libri o autori.
2. Disegna il **modello ER** in Mermaid, indicando chiavi primarie, chiavi esterne e cardinalità minime e massime. Evidenzia gli attributi facoltativi.
3. Disegna il **diagramma delle classi UML** in Mermaid, con attributi, tipi e molteplicità coerenti con il testo.
4. Descrivi separatamente i vincoli che non sono espressi direttamente dai diagrammi, in particolare quello sui prestiti non ancora restituiti.
5. Verifica che il tuo modello consenta sia a un iscritto sia a una copia di esistere senza prestiti e che conservi lo storico dopo una restituzione.

Lavora in `student.md`. Non sono richiesti diagrammi di sequenza, codice Python o test.
