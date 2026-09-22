# Design Esercizio 06: Dominio Magazzino (Soluzione di Riferimento)

## 1. Modello ER (Database su Disco)

```mermaid
erDiagram
    ARTICOLO_MAGAZZINO {
        string codice_sku PK "Codice SKU univoco di magazzino"
        string nome "Denominazione commerciale"
        float prezzo_unitario "Prezzo unitario di vendita in Euro"
        int quantita_disponibile "Pezzi fisicamente a scaffale"
        int scorta_minima "Soglia minima di allerta riordino"
    }
```

---

## 2. Diagramma delle Classi UML (RAM)

```mermaid
classDiagram
    class ArticoloMagazzino {
        +codice_sku: str
        +nome: str
        +prezzo_unitario: float
        +quantita_disponibile: int
        +scorta_minima: int
        +scarica(quantita: int) bool
        +rifornisci(quantita: int) bool
        +sotto_scorta() bool
        +valore_inventario() float
    }
```
