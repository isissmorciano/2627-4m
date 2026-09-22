# Esercizio 06: Dominio Magazzino — Giacenze, Scorta Minima e Valore

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 e Cap. 03 - Dataclass, Metodi di stato e Calcoli)  
> **Obiettivo**: Modellare e implementare un'entità per la gestione delle scorte (`ArticoloMagazzino`) con controlli di disponibilità, rilevamento automatico del sottoscorta e calcolo del valore monetario di inventario.

---

## 1. Il Contesto di Business

Nella logistica e nel commercio elettronico, ogni articolo deve garantire l'integrità della giacenza: non è possibile vendere merce che non è fisicamente presente a scaffale (*rottura di stock*), ed è fondamentale monitorare quando i pezzi scendono sotto una soglia di sicurezza (*scorta minima*) per inviare l'ordine di riassortimento al fornitore.

> **User Story:**  
> *«Come Gestore del Magazzino, voglio registrare i movimenti di carico e scarico di un articolo, per mantenere aggiornata la giacenza reale ed essere avvisato tempestivamente quando la merce è in esaurimento.»*

### Criteri di Accettazione (Definition of Done)
- [ ] Ogni articolo è identificato univocamente da una Primary Key `codice_sku` (stringa, codice alfanumerico di magazzino, es. `"SKU-TECH-01"`).
- [ ] L'articolo memorizza il `nome` (stringa), il `prezzo_unitario` (decimale), la `quantita_disponibile` (intero, default 0) e la `scorta_minima` (intero, default 5).
- [ ] Il metodo `scarica(quantita: int) -> bool`:
  - Se `0 < quantita <= quantita_disponibile`: decrementa la giacenza e restituisce `True`.
  - Se `quantita > quantita_disponibile` (merce insufficiente) o `quantita <= 0`: l'operazione viene respinta, la giacenza non viene modificata e restituisce `False`.
- [ ] Il metodo `rifornisci(quantita: int) -> bool`:
  - Se `quantita > 0`: incrementa la giacenza e restituisce `True`.
  - Se `quantita <= 0`: restituisce `False` senza alterare la giacenza.
- [ ] Il metodo `sotto_scorta() -> bool`:
  - Restituisce `True` se `quantita_disponibile <= scorta_minima`, altrimenti `False`.
- [ ] Il metodo `valore_inventario() -> float`:
  - Calcola e restituisce il valore economico complessivo a magazzino (`quantita_disponibile * prezzo_unitario`), arrotondato a due decimali.

---

## 2. Consegna dell'Esercizio

### Parte 1 — Modellazione Statica (`es06_student.md`)
Disegna in Mermaid:
1. **Diagramma ER:** Entità `ARTICOLO_MAGAZZINO` con `string codice_sku PK`, `string nome`, `float prezzo_unitario`, `int quantita_disponibile`, `int scorta_minima`.
2. **Class Diagram UML:** Classe `ArticoloMagazzino` con attributi tipizzati in Python e metodi `scarica`, `rifornisci`, `sotto_scorta`, `valore_inventario`.

### Parte 2 — Implementazione in Python (`es06_student.py`)
1. Implementa la classe con `@dataclass`.
2. Implementa i metodi operativi garantendo la protezione della giacenza.
3. Nella funzione `main()`:
   - Crea un articolo "Tastiera Meccanica" (prezzo 75.00€, quantità iniziale 12 pezzi, scorta minima 5).
   - Mostra il valore totale dell'inventario iniziale (12 * 75.00 = 900.00€).
   - Esegui uno scarico di 8 pezzi: mostra che l'operazione ha successo (rimangono 4 pezzi).
   - Dimostra che il metodo `sotto_scorta()` ora segnala l'allarme (`True`) perché 4 <= 5.
   - Tenta uno scarico eccessivo di 10 pezzi: dimostra che viene respinto (`False`) e che la giacenza resta 4.
   - Esegui un riassortimento di 20 pezzi e verifica che l'allarme sottoscorta si disattivi (`False`).

---

## 3. Esempio di Esecuzione del `main()`
```text
=== GESTIONE SCORTE MAGAZZINO ===
Articolo SKU-TECH-01: Tastiera Meccanica
Prezzo: 75.00€ | Giacenza: 12 pezzi | Scorta Minima: 5
Valore inventario iniziale: 900.00€ | Sotto scorta? False

Scarico 8 pezzi (vendita) -> Esito: True
Nuova giacenza: 4 pezzi
ATTENZIONE: Articolo sotto scorta! (sotto_scorta: True)

Tentativo scarico 10 pezzi (richiesta oltre stock) -> Esito: False
Operazione respinta: merce insufficiente!
Giacenza inalterata: 4 pezzi

Rifornimento fornitore (+20 pezzi) -> Esito: True
Nuova giacenza: 24 pezzi | Sotto scorta? False
Valore inventario aggiornato: 1800.00€
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es06.py
```
