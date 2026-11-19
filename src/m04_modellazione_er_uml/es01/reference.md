# Esercizio 01: Prestiti in biblioteca — Soluzione di riferimento

## Modello ER

```mermaid
erDiagram
    ISCRITTO ||--o{ PRESTITO : effettua
    COPIA ||--o{ PRESTITO : riguarda

    ISCRITTO {
        int numero_tessera PK
        string nome
        string cognome
    }
    COPIA {
        int codice PK
        string titolo
        string autore
    }
    PRESTITO {
        int id PK
        int numero_tessera FK
        int codice_copia FK
        date data_inizio
        date data_scadenza_prevista
        date data_restituzione "Facoltativa"
    }
```

## Diagramma delle classi UML

```mermaid
classDiagram
    Iscritto "1" -- "0..*" Prestito : effettua
    Copia "1" -- "0..*" Prestito : riguarda

    class Iscritto {
        +numero_tessera: int
        +nome: string
        +cognome: string
    }
    class Copia {
        +codice: int
        +titolo: string
        +autore: string
    }
    class Prestito {
        +id: int
        +data_inizio: date
        +data_scadenza_prevista: date
        +data_restituzione: date [0..1]
    }
```

## Vincoli

- Ogni prestito fa riferimento obbligatoriamente a un iscritto e a una copia esistenti. Iscritti e copie possono esistere anche senza prestiti.
- La data di restituzione è assente finché il prestito è attivo. Per una copia può esistere al massimo un prestito senza data di restituzione: questo vincolo condizionale non è rappresentato dalle sole cardinalità.
- Un vincolo `UNIQUE` sulla sola chiave esterna della copia non sarebbe corretto: impedirebbe anche di conservare più prestiti conclusi della stessa copia.
