# Esercizio 03: Relazione 1-a-Molti — Foreign Key sul lato Molti e `default_factory=list`

> **Prerequisiti teorici**: Modulo 02 (Cap. 03 - Associazione 1-a-Molti: Collezioni di Oggetti e Sequenza)  
> **Obiettivo**: Modellare la relazione 1:N posizionando la FK sul lato Molti in ER, e implementare in Python la collezione tramite `field(default_factory=list)` garantendo il rispetto della capienza massima.

---

## 1. Il Contesto di Business

Uno `Zaino` contiene una collezione di `Oggetto` (pozioni, armi).

### Criteri di Accettazione (Definition of Done)
- [ ] Nel modello ER, la Foreign Key `inventario_id FK` si trova nella tabella `OGGETTO` (lato Molti).
- [ ] La classe `Inventario` memorizza gli oggetti in `oggetti_contenuti: list[Oggetto] = field(default_factory=list)`.
- [ ] Il metodo `aggiungi_oggetto(ogg: Oggetto) -> bool`:
  - Se `len(oggetti_contenuti) < capacita_slot`: aggiunge l'oggetto e restituisce `True`.
  - Se lo zaino è al completo (`>= capacita_slot`): rifiuta l'oggetto e restituisce `False`.
- [ ] Il metodo `conta_oggetti() -> int` restituisce il numero di oggetti presenti.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== GESTIONE ZAINO (RELAZIONE 1:N) ===
Zaino #1 creato (Capacita: 2 slot | Oggetti iniziali: 0)

Aggiunta Spada -> Esito: True (Slot occupati: 1/2)
Aggiunta Pozione -> Esito: True (Slot occupati: 2/2)
Tentativo aggiunta Scudo (zaino pieno) -> Esito: False
Slot occupati inalterati: 2/2
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es03.py
```
