# Design Esercizio 01: Relazione 1-a-1 (Eroe e Zaino)

## 1. Modello ER (Database su Disco)

```mermaid
erDiagram
    PERSONAGGIO ||--|| INVENTARIO : possiede

    PERSONAGGIO {
        int id PK
        string nome
        int livello
    }
    INVENTARIO {
        int id PK
        %% Inserisci qui la Foreign Key con UNIQUE e la capacita_slot
    }
```

---

## 2. Diagramma di Sequenza (Dinamica)

```mermaid
sequenceDiagram
    autonumber
    actor Giocatore as 👤 Giocatore
    participant Eroe as eroe :Personaggio
    participant Zaino as zaino :Inventario

    %% Completa le frecce dello scambio di messaggi per assegna_inventario
```

---

## 3. Diagramma delle Classi UML (RAM)

```mermaid
classDiagram
    %% Disegna qui le classi Personaggio e Inventario con la relazione "1" -- "1"
```
