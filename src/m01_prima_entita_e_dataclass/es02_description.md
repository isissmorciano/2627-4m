# Esercizio 02: Mappatura Tipi ER ↔ Python e Passaggio a @dataclass

> **Prerequisiti teorici**: Modulo 01 (Cap. 03 - Evoluzione Moderna: Dataclass)  
> **Obiettivo**: Comprendere la corrispondenza dei tipi tra Database (ER) e Python (UML), ed eliminare il codice ripetitivo riscrivendo l'entità con `@dataclass`.

---

## 1. Perché passare alle `@dataclass`?

Nella classe tradizionale di `es01` abbiamo dovuto scrivere a mano:
```python
self.id = id_personaggio
self.nome = nome
self.livello = livello
self.punti_vita = 100
```
Se un'entità ha 8 o 10 attributi, questo lavoro diventa noioso e fonte di errori (*codice boilerplate*).

Inoltre, con le classi tradizionali due oggetti con gli stessi identici valori risultano **diversi** con `==`:
```python
p1 = Personaggio(1, "Aragorn")
p2 = Personaggio(1, "Aragorn")
print(p1 == p2)  # False! (perché Python confronta gli indirizzi di memoria RAM)
```

Il decoratore standard **`@dataclass`** risolve entrambi i problemi:
1. Genera automaticamente il costruttore `__init__` leggendo le annotazioni di tipo.
2. Genera una rappresentazione tecnica chiara (`__repr__`).
3. Genera il confronto per valore (`__eq__`): due oggetti con gli stessi campi risulteranno finalmente **uguali** (`p1 == p2 -> True`).

---

## 2. La Mappatura dei Tipi (Database vs Python)

Prima di scrivere il codice, dobbiamo mappare con precisione i tipi relazionali dell'ER nei tipi corrispondenti di Python:

| Tipo nel Database (ER) | Tipo in Python (UML e Codice) | Note |
| :--- | :--- | :--- |
| `int` | `int` | Numeri interi (ID, livelli, contatori) |
| `string` | `str` | Testo (nomi, descrizioni, codici) |
| `float` / `decimal` | `float` | Numeri con la virgola (prezzi, coordinate) |
| `boolean` | `bool` | Valori di verità (`True` o `False`) |

---

## 3. Consegna dell'Esercizio

### Parte 1 — Modellazione Statica (`es02_student.md`)
1. **Modello ER:** Disegna l'entità `PERSONAGGIO` con Primary Key `id PK`, `nome string`, `livello int`, `punti_vita int`.
2. **Class Diagram UML:** Disegna la classe `Personaggio` con attributi tipizzati in Python e il metodo `presentati() -> str`.

### Parte 2 — Implementazione con `@dataclass` (`es02_student.py`)
1. Importa `dataclass` da `dataclasses`.
2. Decora la classe con `@dataclass`.
3. Dichiara i campi con Type Hints e valori di default (`livello: int = 1`, `punti_vita: int = 100`).
4. Implementa il metodo `presentati(self) -> str`.
5. Nella funzione `main()`:
   - Crea due eroi gemelli (`eroe_a` ed `eroe_b`) con lo stesso id e nome.
   - Dimostra con `print(eroe_a == eroe_b)` che `@dataclass` li riconosce come uguali (`True`).
   - Stampa direttamente un oggetto con `print(eroe_a)` per osservare il `__repr__` automatico generato.

---

## 4. Esempio di Esecuzione del `main()`
```text
=== TEST UGUAGLIANZA E RAPPRESENTAZIONE DATACLASS ===
Rappresentazione automatica eroe_a:
Personaggio(id=1, nome='Aragorn', livello=1, punti_vita=100)

Confronto eroe_a == eroe_b (stessi dati):
True

Confronto eroe_a == eroe_c (dati diversi):
False
```

---

## 5. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es02.py
```
