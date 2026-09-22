# Design Esercizio 03: Relazione 1-a-Molti (Soluzione di Riferimento)

## 1. Modello ER

```mermaid
erDiagram
    INVENTARIO ||--|{ OGGETTO : contiene

    INVENTARIO {
        int id PK "ID inventario"
        int capacita_slot "Capacita massima"
    }
    OGGETTO {
        int id PK "ID oggetto"
        int inventario_id FK "Punta a INVENTARIO.id"
        string nome "Nome oggetto"
        string tipo "Categoria"
    }
```

---

## 2. Diagramma delle Classi UML

```mermaid
classDiagram
    Inventario "1" -- "*" Oggetto : contiene

    class Inventario {
        +id: int
        +capacita_slot: int
        +oggetti_contenuti: list~Oggetto~
        +aggiungi_oggetto(ogg: Oggetto) bool
        +conta_oggetti() int
    }

    class Oggetto {
        +id: int
        +nome: str
        +tipo: str
    }
```
