# Design Progetto 02: Centro Sportivo (Soluzione di Riferimento)

```mermaid
erDiagram
    PRENOTAZIONE }|--|| CAMPO : riguarda
    PRENOTAZIONE ||--|{ NOLEGGIO_ATTREZZATURA : include
    ATTREZZATURA ||--|{ NOLEGGIO_ATTREZZATURA : noleggiata_in

    CAMPO {
        string codice_campo PK
        string sport
        float tariffa_oraria
    }
    PRENOTAZIONE {
        int id_prenotazione PK
        string cliente
        string campo_codice FK
        string data_ora
    }
    NOLEGGIO_ATTREZZATURA {
        int id PK
        int prenotazione_id FK
        int attrezzatura_id FK
        int quantita
    }
    ATTREZZATURA {
        int id PK
        string nome
        float tariffa_oraria
    }
```