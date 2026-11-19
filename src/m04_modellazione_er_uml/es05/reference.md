# Esercizio 05: Soluzione di riferimento

```mermaid
erDiagram
    PALCO ||--o{ CONCERTO : ospita
    ARTISTA ||--o{ INGAGGIO : riceve
    CONCERTO ||--o{ INGAGGIO : prevede
    SPETTATORE ||--o{ BIGLIETTO : possiede
    CONCERTO ||--o{ BIGLIETTO : riguarda
    CATEGORIA ||--o{ BIGLIETTO : classifica
    PALCO {
        int codice PK
        string nome
        int capienza
    }
    CONCERTO {
        int codice PK
        string titolo
        datetime data_ora
        int palco_codice FK
    }
    ARTISTA {
        int codice PK
        string nome_arte
    }
    INGAGGIO {
        int id PK
        int artista_codice FK
        int concerto_codice FK
        string ruolo
    }
    SPETTATORE {
        int codice PK
        string nome
    }
    BIGLIETTO {
        int numero PK
        int spettatore_codice FK
        int concerto_codice FK
        int categoria_codice FK
    }
    CATEGORIA {
        int codice PK
        string nome
        decimal prezzo
    }
```

```mermaid
classDiagram
    Palco "1" -- "0..*" Concerto : ospita
    Artista "1" -- "0..*" Ingaggio : riceve
    Concerto "1" -- "0..*" Ingaggio : prevede
    Spettatore "1" -- "0..*" Biglietto : possiede
    Concerto "1" -- "0..*" Biglietto : riguarda
    Categoria "1" -- "0..*" Biglietto : classifica
    class Palco {
        +codice: int
        +nome: string
        +capienza: int
    }
    class Concerto {
        +codice: int
        +titolo: string
        +data_ora: datetime
    }
    class Artista {
        +codice: int
        +nome_arte: string
    }
    class Ingaggio {
        +id: int
        +ruolo: string
    }
    class Spettatore {
        +codice: int
        +nome: string
    }
    class Biglietto {
        +numero: int
    }
    class Categoria {
        +codice: int
        +nome: string
        +prezzo: decimal
    }
```

- La coppia artista-concerto è univoca. Il conteggio dei biglietti di un concerto non può superare la capienza del relativo palco: le cardinalità da sole non impongono questo vincolo.
