# Esercizio 04: Test Round-Trip e Detective della Persistenza

> **Prerequisiti teorici**: Modulo 04 (Tutti i capitoli)  
> **Obiettivo**: Scrivere una suite Pytest completa di collaudo *Round-Trip* (RAM $\to$ File $\to$ RAM) con la fixture `tmp_path` e correggere un gestore difettoso che corrompe i tipi in fase di caricamento.

---

## 1. Il Test Round-Trip

Il test definitivo di persistenza si chiama **Round-Trip**:
1. Creo un grafo di oggetti in RAM.
2. Eseguo delle operazioni (danni, aggiunte di oggetti).
3. Salvo su file JSON.
4. Ricarico in una seconda variabile indipendente.
5. Verifico che lo stato ricaricato sia identico a quello originale e che i metodi funzionino.

---

## 2. Lo Scenario del Detective

Un programmatore ha scritto `gestore_difettoso.py`. Nel caricare un `Utente` con la sua `Tessera`:
* Salva correttamente con `asdict`.
* In fase di caricamento, ricrea l'utente ma lascia la tessera come semplice `dict` (`utente.tessera` non è un'istanza di `Tessera`!).
* Di conseguenza, invocare `utente.tessera.valida()` causa un crash `AttributeError: 'dict' object has no attribute 'valida'`.

---

## 3. Consegna dell'Esercizio

Apri `es04_student.md` ed `es04_student.py`:
1. Compila il **Verdetto del Detective** spiegando perché lasciare dizionari grezzi annidati distrugge l'incapsulamento OOP.
2. Correggi la funzione `carica_utente(percorso: str) -> Utente` in `es04_student.py` ripristinando la vera istanza di `Tessera`.
3. Dimostra nel `main()` che il metodo `utente.tessera.valida()` funziona perfettamente dopo la ricarica.

---

## 4. Verifica del Lavoro
```bash
pytest tests/test_m04_persistenza/test_es04.py
```
