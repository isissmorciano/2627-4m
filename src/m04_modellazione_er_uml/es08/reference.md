# Esercizio 08: Soluzione di riferimento

```mermaid
erDiagram
    PERSONAGGIO ||--o| INVENTARIO : possiede
    INVENTARIO o|--o{ OGGETTO : contiene
    PERSONAGGIO ||--o{ ABILITA_APPRESA : apprende
    ABILITA ||--o{ ABILITA_APPRESA : descrive
    PERSONAGGIO ||--o{ PARTECIPAZIONE : effettua
    MISSIONE ||--o{ PARTECIPAZIONE : prevede
    PARTECIPAZIONE ||--o{ RICOMPENSA : ottiene
    PERSONAGGIO ||--o{ ISCRIZIONE_GILDA : effettua
    GILDA ||--o{ ISCRIZIONE_GILDA : riceve
    PERSONAGGIO {
        int id PK
        string nome
        int livello
    }
    INVENTARIO {
        int codice PK
        int capacita_slot
        int personaggio_id FK "UNIQUE"
    }
    OGGETTO {
        int id PK
        string nome
        string tipo
        int inventario_codice FK "Facoltativo"
    }
    ABILITA {
        int id PK
        string nome
        int costo_mana
    }
    ABILITA_APPRESA {
        int id PK
        int personaggio_id FK
        int abilita_id FK
        int livello_padronanza
    }
    MISSIONE {
        int codice PK
        string titolo
    }
    PARTECIPAZIONE {
        int id PK
        int personaggio_id FK
        int missione_codice FK
        date data
        string ruolo
    }
    RICOMPENSA {
        int codice PK
        string descrizione
        int quantita
        int partecipazione_id FK
    }
    GILDA {
        int codice PK
        string nome
    }
    ISCRIZIONE_GILDA {
        int id PK
        int personaggio_id FK
        int gilda_codice FK
        date data_ingresso
        date data_uscita "Facoltativa"
    }
```

```mermaid
classDiagram
    Personaggio "1" -- "0..1" Inventario : possiede
    Inventario "0..1" -- "0..*" Oggetto : contiene
    Personaggio "1" -- "0..*" AbilitaAppresa : apprende
    Abilita "1" -- "0..*" AbilitaAppresa : descrive
    Personaggio "1" -- "0..*" Partecipazione : effettua
    Missione "1" -- "0..*" Partecipazione : prevede
    Partecipazione "1" -- "0..*" Ricompensa : ottiene
    Personaggio "1" -- "0..*" IscrizioneGilda : effettua
    Gilda "1" -- "0..*" IscrizioneGilda : riceve
    class Personaggio {
        +id: int
        +nome: string
        +livello: int
    }
    class Inventario {
        +codice: int
        +capacita_slot: int
    }
    class Oggetto {
        +id: int
        +nome: string
        +tipo: string
    }
    class Abilita {
        +id: int
        +nome: string
        +costo_mana: int
    }
    class AbilitaAppresa {
        +id: int
        +livello_padronanza: int
    }
    class Missione {
        +codice: int
        +titolo: string
    }
    class Partecipazione {
        +id: int
        +data: date
        +ruolo: string
    }
    class Ricompensa {
        +codice: int
        +descrizione: string
        +quantita: int
    }
    class Gilda {
        +codice: int
        +nome: string
    }
    class IscrizioneGilda {
        +id: int
        +data_ingresso: date
        +data_uscita: date [0..1]
    }
```

- La FK dell'inventario verso il personaggio è obbligatoria e univoca; quella dell'oggetto verso l'inventario è facoltativa. Il numero di oggetti non deve superare la capacità.
- Sono univoche le coppie personaggio-abilità e personaggio-missione; la padronanza è compresa tra 1 e 5.
- Per ogni personaggio può esistere al massimo un'iscrizione senza data di uscita. Un `UNIQUE` sulla sola FK del personaggio impedirebbe erroneamente di conservare lo storico.
