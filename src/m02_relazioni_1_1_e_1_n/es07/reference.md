# Design Esercizio 07: Pipeline Completa Hotel e Stanze (Soluzione di Riferimento)

## 1. Requisiti e User Story

**Come** Receptionist dell'albergo  
**voglio** assegnare una camera libera della tipologia richiesta a un cliente  
**per** registrarne il soggiorno garantendo che nessuna stanza venga prenotata due volte  

### Criteri di Accettazione
- [ ] Nel modello ER la Foreign Key `hotel_nome FK` è posizionata nella tabella `STANZA` (lato Molti).
- [ ] L'hotel cerca la prima camera disponibile con `tipo == tipo_richiesto` e `is_occupata == False`.
- [ ] Se disponibile, la camera passa a `is_occupata = True` e viene restituita.
- [ ] Se non ci sono camere libere del tipo richiesto, l'operazione restituisce `None`.

---

## 2. Modello ER

```mermaid
erDiagram
    HOTEL ||--|{ STANZA : gestisce

    HOTEL {
        string nome PK
    }
    STANZA {
        int numero PK
        string hotel_nome FK
        string tipo
        float prezzo
        boolean is_occupata
    }
```

---

## 3. Diagramma di Sequenza

```mermaid
sequenceDiagram
    autonumber
    actor Rec as 👤 Receptionist
    participant H as hotel :Hotel
    participant S as stanza :Stanza

    Rec->>H: prenota_camera("Doppia")
    activate H
    H->>S: verifica is_occupata == False
    S-->>H: disponibile
    Note over S: is_occupata = True
    H-->>Rec: stanza assegnata
    deactivate H
```
