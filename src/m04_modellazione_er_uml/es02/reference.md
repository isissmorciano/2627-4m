# Esercizio 02: Soluzione di riferimento

```mermaid
erDiagram
    SQUADRA ||--o{ GIOCATORE : comprende
    SQUADRA ||--o{ PARTITA : casa
    SQUADRA ||--o{ PARTITA : trasferta
    GIOCATORE ||--o{ CONVOCAZIONE : riceve
    PARTITA ||--o{ CONVOCAZIONE : include
    SQUADRA {
        int codice PK
        string nome
    }
    GIOCATORE {
        int matricola PK
        string nome
        int squadra_codice FK
    }
    PARTITA {
        int codice PK
        date data
        int casa_codice FK
        int trasferta_codice FK
    }
    CONVOCAZIONE {
        int codice PK
        int giocatore_matricola FK
        int partita_codice FK
        string ruolo
        int minuti_giocati
    }
```

```mermaid
classDiagram
    Squadra "1" -- "0..*" Giocatore : comprende
    Squadra "1" -- "0..*" Partita : casa
    Squadra "1" -- "0..*" Partita : trasferta
    Giocatore "1" -- "0..*" Convocazione : riceve
    Partita "1" -- "0..*" Convocazione : include
    class Squadra {
        +codice: int
        +nome: string
    }
    class Giocatore {
        +matricola: int
        +nome: string
    }
    class Partita {
        +codice: int
        +data: date
    }
    class Convocazione {
        +codice: int
        +ruolo: string
        +minuti_giocati: int
    }
```

- Le due squadre della partita devono essere diverse. La coppia giocatore-partita è univoca.
- La squadra del giocatore convocato deve coincidere con quella di casa o di trasferta; questo controllo richiede di confrontare più relazioni.
