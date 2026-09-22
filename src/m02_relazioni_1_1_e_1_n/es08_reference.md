# Design Esercizio 08: Detective delle Relazioni (Soluzione di Riferimento)

## 1. Il Verdetto del Detective

- **Bug 1 (Default Mutabile Condiviso):** Usare una lista mutabile come valore predefinito (`giocatori: list = []`) fa sì che Python crei una sola lista in memoria al momento della definizione della classe, condivisa da tutte le istanze future di `Squadra`. È obbligatorio usare `field(default_factory=list)`.
- **Bug 2 (Violazione Incapsulamento):** Lasciare che il codice chiamante acceda direttamente con `.append()` impedisce di verificare regole di business (es. il tetto massimo di 11 giocatori a referto).
