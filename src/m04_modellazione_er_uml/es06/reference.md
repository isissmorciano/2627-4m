# Esercizio 06: Soluzione di riferimento

```mermaid
erDiagram
    CENTRO ||--o{ CAMPO : possiede
    SOCIO ||--o{ PRENOTAZIONE : effettua
    CAMPO ||--o{ PRENOTAZIONE : riceve
    CENTRO ||--o{ CORSO : organizza
    ISTRUTTORE ||--o{ CORSO : insegna
    SOCIO ||--o{ ISCRIZIONE : effettua
    CORSO ||--o{ ISCRIZIONE : riceve
    CORSO ||--o{ LEZIONE : prevede
    CAMPO ||--o{ LEZIONE : ospita
    CENTRO {
        int codice PK
        string nome
    }
    CAMPO {
        int codice PK
        string tipo
        int centro_codice FK
    }
    SOCIO {
        int numero PK
        string nome
    }
    PRENOTAZIONE {
        int codice PK
        int socio_numero FK
        int campo_codice FK
        datetime inizio
        datetime fine
    }
    ISTRUTTORE {
        int matricola PK
        string nome
    }
    CORSO {
        int codice PK
        string titolo
        int centro_codice FK
        int istruttore_matricola FK
    }
    ISCRIZIONE {
        int id PK
        date data
        int socio_numero FK
        int corso_codice FK
    }
    LEZIONE {
        int codice PK
        datetime data_ora
        int corso_codice FK
        int campo_codice FK
    }
```

```mermaid
classDiagram
    Centro "1" -- "0..*" Campo : possiede
    Socio "1" -- "0..*" Prenotazione : effettua
    Campo "1" -- "0..*" Prenotazione : riceve
    Centro "1" -- "0..*" Corso : organizza
    Istruttore "1" -- "0..*" Corso : insegna
    Socio "1" -- "0..*" Iscrizione : effettua
    Corso "1" -- "0..*" Iscrizione : riceve
    Corso "1" -- "0..*" Lezione : prevede
    Campo "1" -- "0..*" Lezione : ospita
    class Centro {
        +codice: int
        +nome: string
    }
    class Campo {
        +codice: int
        +tipo: string
    }
    class Socio {
        +numero: int
        +nome: string
    }
    class Prenotazione {
        +codice: int
        +inizio: datetime
        +fine: datetime
    }
    class Istruttore {
        +matricola: int
        +nome: string
    }
    class Corso {
        +codice: int
        +titolo: string
    }
    class Iscrizione {
        +id: int
        +data: date
    }
    class Lezione {
        +codice: int
        +data_ora: datetime
    }
```

- La coppia socio-corso è univoca. L'inizio di una prenotazione precede la fine; intervalli di prenotazione dello stesso campo non si sovrappongono.
- Il centro del campo di una lezione deve coincidere con il centro del corso; la sola presenza delle FK non garantisce il vincolo.
