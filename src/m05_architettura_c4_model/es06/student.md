# Design Esercizio 06: Detective Architetturale

## 1. Il Diagramma Difettoso del Collega (Da Analizzare)

```mermaid
flowchart LR
    PAZIENTE[👤 Paziente] --> APP[App Mobile]
    APP --> CLASSE[Classe Prenotazione con metodo valida]
    CLASSE --> BACKEND[Server Python]
    BACKEND --> OSPEDALE_EST[ASL API Esterna]
    BACKEND --> DB[(Database Pazienti)]
    
    %% Nota: Nel diagramma originale DB era disegnato fuori dal sistema!
```

---

## 2. Il Verdetto del Detective

- [ ] **Errore 1 (Errore di Granularità / Livello errato):** [...]
- [ ] **Errore 2 (Confine di Sistema / Boundary violato):** [...]
- [ ] **Errore 3 (Assenza di Dettagli di Comunicazione):** [...]

---

## 3. Diagramma C4 Container Corretto

```mermaid
flowchart LR
    %% Ridisegna qui il Container Diagram corretto con boundary, blocchi e protocolli espliciti
```