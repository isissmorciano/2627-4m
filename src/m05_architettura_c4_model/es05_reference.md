# Design Esercizio 05: Doppio Zoom L1 -> L2 UrbanSport (Soluzione di Riferimento)

## 1. C4 Livello 1: System Context (La Vista Aerea)

```mermaid
flowchart LR
    CLIENTE[👤 Cliente] -->|Consulta catalogo e acquista| US[🛍️ Piattaforma UrbanSport]
    MAGAZZINIERE[👤 Addetto Magazzino] -->|Gestisce spedizioni e inventario| US

    US -->|Elabora transazioni carte| BANK[💳 Gateway Pagamenti]
    US -->|Richiede lettere di vettura e tracking| DHL[🚚 Servizio Spedizioni DHL API]
```

---

## 2. C4 Livello 2: Container (Esploso dei Componenti)

```mermaid
flowchart LR
    CLIENTE[👤 Cliente] -->|HTTPS| STORE_WEB[🌐 Store Web\nE-Commerce UI]
    MAGAZZINIERE[👤 Magazziniere] -->|HTTPS| LOG_WEB[🖥️ Gestionale Magazzino\nWeb UI]

    subgraph URBANSPORT_SYSTEM [Piattaforma UrbanSport]
        STORE_WEB -->|HTTPS / REST API| BACKEND[⚙️ Backend Core API\nPython / Logica di Dominio]
        LOG_WEB -->|HTTPS / REST API| BACKEND

        BACKEND -->|SQL / TCP| DB[(💾 Database Relazionale\nCatalogo e Ordini)]
    end

    BACKEND -->|Chiamate HTTPS/JSON| BANK[💳 Gateway Pagamenti]
    BACKEND -->|Chiamate HTTPS/JSON| DHL[🚚 DHL API]
```