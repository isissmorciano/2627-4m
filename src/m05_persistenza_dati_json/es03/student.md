# Design Esercizio 03: Polimorfismo su Disco

```mermaid
classDiagram
    Personaggio <|-- Guerriero
    Personaggio <|-- Mago

    class Personaggio {
        +id: int
        +nome: str
    }
    class Guerriero {
        +forza: int
    }
    class Mago {
        +mana: int
    }
```

### Struttura JSON con Discriminatore:
```json
[
    {"tipo": "guerriero", "id": 1, "nome": "Conan", "forza": 12},
    {"tipo": "mago", "id": 2, "nome": "Merlino", "mana": 45}
]
```
