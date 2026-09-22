# Design Esercizio 05 (Soluzione di Riferimento)

```mermaid
classDiagram
    Personaggio <|-- Guerriero
    Personaggio <|-- Mago

    class Personaggio {
        +id: int
        +nome: str
        +punti_vita: int
        +subisci_danno(danno: int) None
        +attacca(bersaglio) str
    }
    class Guerriero {
        +forza: int
        +attacca(bersaglio) str
    }
    class Mago {
        +mana: int
        +attacca(bersaglio) str
    }
```
