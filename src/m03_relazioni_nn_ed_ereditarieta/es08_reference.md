# Design Esercizio 08: Detective di Architettura (Soluzione di Riferimento)

## 1. Il Verdetto del Detective

- **Errore 1 (Mancato uso di super):** Senza `super().__init__()`, ogni modifica futura alla classe base `Veicolo` non viene propagata alla classe derivata, generando duplicazione e bug di disallineamento.
- **Errore 2 (HAS-A scambiato per IS-A):** Un motore non è una tipologia di veicolo (non è una relazione IS-A). È una parte componente del veicolo (relazione HAS-A di composizione/associazione).
