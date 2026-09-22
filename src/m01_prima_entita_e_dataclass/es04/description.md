# Esercizio 04: Dominio Bancario — PK Alfanumerica e Transazioni

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - La Chiave Primaria; Cap. 03 - Dataclass e Metodi)  
> **Obiettivo**: Modellare e implementare un'entità di business reale (`ContoCorrente`) con una Primary Key alfanumerica (`iban: str`) e metodi transazionali che restituiscono un esito booleano proteggendo il saldo.

---

## 1. Il Contesto di Business

Usciamo dal mondo RPG ed entriamo nel settore bancario. Finora abbiamo usato identificatori numerici progressivi (`id: int`). Tuttavia, nel mondo reale molte entità usano codici alfanumerici standardizzati come Chiave Primaria (es. Codice Fiscale, Partita IVA, IBAN).

> **User Story:**  
> *«Come Titolare di conto corrente, voglio poter depositare e prelevare denaro dal mio conto, per gestire le mie finanze quotidiane senza rischiare di andare in rosso.»*

### Criteri di Accettazione (Definition of Done)
- [ ] Ogni conto deve essere identificato in modo univoco dal codice `iban` (stringa, Primary Key).
- [ ] Il conto memorizza il nome del `titolare` (stringa) e il `saldo` corrente (decimale, inizialmente pari a 0.0€).
- [ ] Il metodo `deposita(importo: float) -> bool`:
  - Se `importo > 0`: accredita l'importo sul saldo e restituisce `True`.
  - Se `importo <= 0`: rifiuta l'operazione, lascia il saldo intatto e restituisce `False`.
- [ ] Il metodo `preleva(importo: float) -> bool`:
  - Se `importo > 0` e `importo <= saldo`: addebita l'importo e restituisce `True`.
  - Se `importo > saldo` (tentativo di scoperto) oppure `importo <= 0`: rifiuta il prelievo, garantisce l'invarianza del saldo e restituisce `False`.
- [ ] Il metodo `mostra_stato() -> str` restituisce: `"Conto <iban> intestato a <titolare> - Saldo: <saldo:.2f>€"`.

---

## 2. Consegna dell'Esercizio

### Parte 1 — Modellazione Statica (`student.md`)
Disegna in Mermaid:
1. **Diagramma ER:** Entità `CONTO_CORRENTE` con `string iban PK`, `string titolare`, `float saldo`.
2. **Diagramma UML:** Classe `ContoCorrente` con attributi tipizzati in Python e firme dei metodi (`deposita`, `preleva`, `mostra_stato`).

### Parte 2 — Implementazione in Python (`student.py`)
1. Implementa la classe con `@dataclass`.
2. Implementa i metodi transazionali con protezione degli invarianti.
3. Nella funzione `main()`:
   - Apri un conto per "Mario Rossi" con saldo iniziale 0.0€.
   - Esegui un deposito valido di 250.00€ e mostra il saldo aggiornato.
   - Esegui un prelievo valido di 100.00€ (saldo residuo: 150.00€).
   - Tenta un prelievo non autorizzato di 300.00€: dimostra che l'operazione restituisce `False` e che il saldo rimane invariato a 150.00€.

---

## 3. Esempio di Esecuzione del `main()`
```text
=== GESTIONALE CONTO CORRENTE ===
Conto IT99X0123456789 intestato a Mario Rossi - Saldo: 0.00€

Deposito 250.00€ -> Esito: True
Conto IT99X0123456789 intestato a Mario Rossi - Saldo: 250.00€

Prelievo 100.00€ -> Esito: True
Conto IT99X0123456789 intestato a Mario Rossi - Saldo: 150.00€

Tentativo prelievo 300.00€ (scoperto) -> Esito: False
Transazione negata per fondi insufficienti!
Conto IT99X0123456789 intestato a Mario Rossi - Saldo: 150.00€
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es04.py
```
