# Esercizio 04: Soluzione di riferimento

```mermaid
erDiagram
    CLIENTE ||--o{ ORDINE : effettua
    ORDINE ||--|{ RIGA : comprende
    ARTICOLO ||--o{ RIGA : compare
    ORDINE ||--o{ PAGAMENTO : riceve
    ORDINE ||--o| SPEDIZIONE : genera
    CLIENTE {
        int codice PK
        string nome
        string email
    }
    ORDINE {
        int numero PK
        date data
        int cliente_codice FK
    }
    ARTICOLO {
        int codice PK
        string nome
        decimal prezzo_attuale
    }
    RIGA {
        int id PK
        int ordine_numero FK
        int articolo_codice FK
        int quantita
        decimal prezzo_unitario
    }
    PAGAMENTO {
        int id PK
        int ordine_numero FK
        date data
        decimal importo
    }
    SPEDIZIONE {
        int codice PK
        int ordine_numero FK "UNIQUE"
        date data
        string indirizzo
    }
```

```mermaid
classDiagram
    Cliente "1" -- "0..*" Ordine : effettua
    Ordine "1" -- "1..*" Riga : comprende
    Articolo "1" -- "0..*" Riga : compare
    Ordine "1" -- "0..*" Pagamento : riceve
    Ordine "1" -- "0..1" Spedizione : genera
    class Cliente {
        +codice: int
        +nome: string
        +email: string
    }
    class Ordine {
        +numero: int
        +data: date
    }
    class Articolo {
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
        +id: int
        +data: date
        +importo: decimal
    }
    class Spedizione {
        +codice: int
        +data: date
        +indirizzo: string
    }
```

- La coppia ordine-articolo è univoca. Il prezzo nella riga conserva quello applicato, anche se il prezzo di catalogo cambia.
- La FK della spedizione è obbligatoria e univoca; l'ordine può non avere spedizione. La presenza di almeno una riga per ordine richiede un controllo aggiuntivo nel database.
