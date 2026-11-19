# Esercizio 07: Soluzione di riferimento

```mermaid
erDiagram
    SALA ||--o{ TAVOLO : contiene
    CLIENTE ||--o{ PRENOTAZIONE : effettua
    TAVOLO ||--o{ PRENOTAZIONE : riceve
    PRENOTAZIONE ||--o| ORDINE : genera
    CAMERIERE ||--o{ ORDINE : segue
    ORDINE ||--|{ RIGA : comprende
    PIATTO ||--o{ RIGA : compare
    ORDINE ||--o{ PAGAMENTO : riceve
    SALA {
        int codice PK
        string nome
    }
    TAVOLO {
        int numero PK
        int posti
        int sala_codice FK
    }
    CLIENTE {
        int codice PK
        string nome
    }
    PRENOTAZIONE {
        int codice PK
        datetime inizio
        datetime fine
        int persone
        int cliente_codice FK
        int tavolo_numero FK
    }
    CAMERIERE {
        int matricola PK
        string nome
    }
    ORDINE {
        int numero PK
        int prenotazione_codice FK "UNIQUE"
        int cameriere_matricola FK
    }
    PIATTO {
        int codice PK
        string nome
        decimal prezzo_attuale
    }
    RIGA {
        int id PK
        int ordine_numero FK
        int piatto_codice FK
        int quantita
        decimal prezzo_unitario
    }
    PAGAMENTO {
        int codice PK
        date data
        decimal importo
        int ordine_numero FK
    }
```

```mermaid
classDiagram
    Sala "1" -- "0..*" Tavolo : contiene
    Cliente "1" -- "0..*" Prenotazione : effettua
    Tavolo "1" -- "0..*" Prenotazione : riceve
    Prenotazione "1" -- "0..1" Ordine : genera
    Cameriere "1" -- "0..*" Ordine : segue
    Ordine "1" -- "1..*" Riga : comprende
    Piatto "1" -- "0..*" Riga : compare
    Ordine "1" -- "0..*" Pagamento : riceve
    class Sala {
        +codice: int
        +nome: string
    }
    class Tavolo {
        +numero: int
        +posti: int
    }
    class Cliente {
        +codice: int
        +nome: string
    }
    class Prenotazione {
        +codice: int
        +inizio: datetime
        +fine: datetime
        +persone: int
    }
    class Cameriere {
        +matricola: int
        +nome: string
    }
    class Ordine {
        +numero: int
    }
    class Piatto {
        +codice: int
        +nome: string
        +prezzo_attuale: decimal
    }
    class Riga {
        +id: int
        +quantita: int
        +prezzo_unitario: decimal
    }
    class Pagamento {
        +codice: int
        +data: date
        +importo: decimal
    }
```

- La FK dell'ordine verso la prenotazione è obbligatoria e univoca. La coppia ordine-piatto è univoca; il prezzo della riga conserva quello applicato.
- La prenotazione deve terminare dopo l'inizio, non sovrapporsi alle altre dello stesso tavolo e rispettarne il numero di posti. L'ordine deve avere almeno una riga: sono necessari controlli aggiuntivi.
