# Design Esercizio 08: Detective di Classe (Camera Hotel)

## 1. I Modelli Difettosi del Collega (Da Analizzare)

```mermaid
erDiagram
    CAMERA_HOTEL {
        int numero_camera "Numero della stanza (ATTENZIONE: manca qualcosa?)"
        string tipo_camera "Tipologia"
        float tariffa_giornaliera "Prezzo notte"
        boolean is_occupata "Stato camera"
    }
```

```mermaid
classDiagram
    class CameraHotel {
        +numero_camera: int
        +tipo: str
        +tariffa_giornaliera: float
        +is_occupata: bool
        -check_in() void
        +check_out() bool
        +applica_sconto(percentuale: float) bool
    }
```

---

## 2. Il Verdetto del Detective

<!-- 
Identifica e spiega i 3 difetti presenti nel lavoro del collega:
1. Errore nel modello ER.
2. Errore nel Class Diagram UML.
3. Bug logico nel codice Python.
-->

- [ ] **Difetto 1 (Modello ER):** [...]
- [ ] **Difetto 2 (Diagramma UML):** [...]
- [ ] **Difetto 3 (Codice Python e Invarianti):** [...]

---

## 3. I Modelli Corretti (Mermaid)

### Diagramma ER Corretto
```mermaid
erDiagram
    %% Disegna qui il diagramma ER corretto con la PK obbligatoria
```

### Class Diagram UML Corretto
```mermaid
classDiagram
    %% Disegna qui il diagramma UML con visibilita e firme corrette
```
