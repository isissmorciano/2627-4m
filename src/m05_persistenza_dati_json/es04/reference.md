# Design Esercizio 04 (Soluzione di Riferimento)

## 1. Il Verdetto del Detective

- **Difetto di Deserializzazione:** Passare direttamente `Utente(**dati)` lascia l'attributo `tessera` come dizionario Python `{'codice': '...', 'ingressi': 10}`.
- **Rischio Architetturale:** L'oggetto `Utente` perde la capacità di invocare i metodi del componente `tessera.valida()`, trasformando la programmazione a oggetti in una manipolazione fragile di dizionari procedurali.
