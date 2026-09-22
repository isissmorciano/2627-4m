# Esercizio 04: Ereditarietà Pragmatica (IS-A) e la Funzione `super()`

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Ereditarietà Pragmatica IS-A e Polimorfismo)  
> **Obiettivo**: Comprendere e implementare la specializzazione tramite ereditarietà a 1 livello, riutilizzando il costruttore della superclasse con `super().__init__()` e aggiungendo attributi dedicati.

---

## 1. Il Contesto di Business

Invece di creare classi separate duplicando campi comuni (`id`, `nome`, `punti_vita`), creiamo una gerarchia:
* `Personaggio` è la superclasse base.
* `Guerriero` **è un** `Personaggio` ed estende con l'attributo `forza: int`.
* `Mago` **è un** `Personaggio` ed estende con l'attributo `mana: int`.

### Criteri di Accettazione (Definition of Done)
- [ ] `Personaggio` ha `id: int`, `nome: str`, `punti_vita: int = 100`.
- [ ] `Guerriero` eredita da `Personaggio`, invoca `super().__init__(id_personaggio, nome, punti_vita)` e aggiunge `forza: int`.
- [ ] `Mago` eredita da `Personaggio`, invoca `super().__init__(id_personaggio, nome, punti_vita)` e aggiunge `mana: int = 50`.
- [ ] Con la funzione standard `isinstance()`, ogni guerriero e mago deve essere riconosciuto sia come istanza della propria classe sia come istanza di `Personaggio`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== GERARCHIA EROI (IS-A) ===
Guerriero creato: Conan (ID: 1, PV: 120, Forza: 15)
Mago creato: Merlino (ID: 2, PV: 80, Mana: 50)

Verifica polimorfica di tipo:
- Conan e' un Guerriero? True
- Conan e' un Personaggio? True
- Merlino e' un Mago? True
- Merlino e' un Personaggio? True
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es04.py
```
