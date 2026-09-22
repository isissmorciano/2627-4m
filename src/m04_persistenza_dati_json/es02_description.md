# Esercizio 02: Persistenza di Collezioni 1:N — Ricostruire Oggetti da Liste di Dict

> **Prerequisiti teorici**: Modulo 04 (Cap. 02 - Deserializzazione di relazioni complesse)  
> **Obiettivo**: Imparare a deserializzare una relazione 1:N: quando riapriamo un file JSON, gli elementi di una lista tornano come semplici dizionari (`dict`); dobbiamo ricostruire manualmente le vere istanze `@dataclass` interne.

---

## 1. Il Problema della Deserializzazione Annidata

Quando salviamo uno `Zaino` con dentro degli `Oggetto`, `asdict()` trasforma tutto in:
```json
{
    "id": 101,
    "capacita_slot": 10,
    "oggetti": [
        {"id": 1, "nome": "Spada", "tipo": "Arma"},
        {"id": 2, "nome": "Pozione", "tipo": "Cura"}
    ]
}
```
Quando rileggiamo con `json.load()`, la chiave `"oggetti"` è una lista di **dizionari Python grezzi**, non di istanze di `Oggetto`!  
Se non interveniamo, chiamare metodi sugli oggetti interni causerà un crash (`AttributeError`).

Dobbiamo estrarre la lista di dizionari e fare una *list comprehension* ricostruttiva:
```python
oggetti_ricostruiti = [Oggetto(**item) for item in dati["oggetti"]]
```

---

## 2. Esempio di Esecuzione del `main()`
```text
=== PERSISTENZA RELAZIONE 1:N (ZAINO E OGGETTI) ===
Salvataggio zaino con 2 oggetti completato!

--- Ricaricamento e ricostruzione ---
Zaino ricaricato #101 (Capienza: 5 slot)
Numero oggetti ricostruiti: 2
- Oggetto 1: Spada (Tipo: Arma) -> isinstance(Oggetto): True
- Oggetto 2: Pozione (Tipo: Cura) -> isinstance(Oggetto): True
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m04_persistenza/test_es02.py
```
