# Esercizio 06: Dominio Istruzione — `ClasseScolastica` e `Studente` con Filtri

> **Prerequisiti teorici**: Modulo 02 (Cap. 03 - Relazione 1:N e query su oggetti)  
> **Obiettivo**: Modellare una classe contenitore (`ClasseScolastica`) che gestisce una collezione di `Studente`, implementando metodi di calcolo media e filtraggio senza esporre la lista grezza interna.

---

## 1. Il Contesto di Business

Una `ClasseScolastica` ha una capienza massima e contiene molti `Studenti`.

### Criteri di Accettazione (Definition of Done)
- [ ] `Studente` ha `matricola: int`, `nome: str`, `media_voti: float`.
- [ ] `ClasseScolastica` ha `sezione: str`, `capienza_massima: int = 25`, `studenti: list[Studente] = field(default_factory=list)`.
- [ ] `iscrivi_studente(s: Studente) -> bool`:
  - Se `len(studenti) < capienza_massima`: aggiunge e restituisce `True`.
  - Se classe piena: restituisce `False`.
- [ ] `calcola_media_classe() -> float`: media dei voti di tutti gli studenti (arrotondata a 2 decimali). Se vuota restituisce 0.0.
- [ ] `elenco_promossi() -> list[str]`: restituisce una **nuova lista di soli nomi** degli studenti con `media_voti >= 6.0`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== GESTIONALE SCOLASTICO (1:N) ===
Classe 4A Informatica creata (Capienza: 25)

Iscritto: Mario Rossi (Media: 7.5)
Iscritto: Anna Bianchi (Media: 5.5)
Iscritto: Luca Verdi (Media: 8.0)

Media generale classe: 7.00
Studenti promossi: ['Mario Rossi', 'Luca Verdi']
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es06.py
```
