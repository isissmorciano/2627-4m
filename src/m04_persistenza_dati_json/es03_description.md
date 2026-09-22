# Esercizio 03: Polimorfismo su Disco — Il Campo Discriminatore

> **Prerequisiti teorici**: Modulo 04 (Cap. 02 - Ereditarietà e persistenza)  
> **Obiettivo**: Salvare e ripristinare una lista eterogenea di oggetti polimorfici (`Guerriero` e `Mago`) introducendo un campo *discriminatore* nel JSON per ricostruire l'esatta sottoclasse di appartenenza.

---

## 1. Il Problema del Tipo Perduto

Un file JSON memorizza campi, ma non ricorda la classe Python originaria.  
Se salviamo una lista con un Guerriero (`forza=15`) e un Mago (`mana=40`), al caricamento come facciamo a sapere quale classe istanziare?

La tecnica standard nell'ingegneria del software è l'inserimento di un **campo discriminatore** (es. `"tipo_classe": "guerriero" | "mago"`):
* In fase di salvataggio: aggiungiamo `"tipo_classe": "guerriero"` se `isinstance(eroe, Guerriero)`, oppure `"mago"`.
* In fase di caricamento: leggiamo `tipo_classe` e con un `if/elif` istanziamo la classe corretta.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== PERSISTENZA POLIMORFICA (CAMPO DISCRIMINATORE) ===
Squadra originale creata:
- Guerriero: Conan (Forza: 12)
- Mago: Merlino (Mana: 45)

Salvataggio su 'squadra.json' completato!

--- Ricaricamento polimorfico ---
Eroi ricostruiti:
1. Conan -> Tipo esatto: Guerriero | Forza: 12
2. Merlino -> Tipo esatto: Mago | Mana: 45

Verifica polimorfismo post-ricarica:
- Conan attacca Bersaglio -> ⚔️ Conan sferra un colpo potente da 22 danni!
- Merlino attacca Bersaglio -> ✨ Merlino lancia un dardo magico da 25 danni!
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m04_persistenza/test_es03.py
```
