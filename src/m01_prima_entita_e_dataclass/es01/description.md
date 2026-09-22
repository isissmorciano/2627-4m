# Esercizio 01: La Prima Entità — Dal Modello alla Classe Tradizionale

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 - Dall'Entità alla Classe Tradizionale)  
> **Obiettivo**: Modellare la prima entità sia su disco (ER) che in memoria RAM (UML), implementando la classe tradizionale con `__init__`, `self`, `__str__` e una funzione `main()` dimostrativa.

---

## 1. Il Contesto di Business

All'interno del nostro videogioco di ruolo (RPG), dobbiamo realizzare il nucleo fondamentale per la gestione degli eroi.

> **User Story:**  
> *«Come Giocatore, voglio creare il mio personaggio iniziale con un nome, un livello di partenza e i punti vita, per poter iniziare l'avventura nel mondo di gioco.»*

### Criteri di Accettazione (Definition of Done)
- [ ] Ogni eroe deve avere un identificatore univoco obbligatorio (`id`).
- [ ] Ogni eroe possiede un `nome` testuale, un `livello` (inizialmente pari a 1) e `punti_vita` (inizialmente 100).
- [ ] Il metodo `presentati()` restituisce una stringa nel formato: `"Sono <nome>, eroe di livello <livello> con <punti_vita> PV."`
- [ ] Il metodo dunder `__str__()` restituisce la rappresentazione sintetica: `"Personaggio #<id>: <nome> (PV: <punti_vita>/100)"`
- [ ] Le istanze create devono essere completamente indipendenti in memoria RAM.

---

## 2. Consegna dell'Esercizio

L'esercizio è diviso in due parti:

### Parte 1 — Modellazione Statica (`student.md`)
Apri il file `student.md` e completa:
1. **Il Modello ER (Tabella su disco):** definisci l'entità `PERSONAGGIO` completando la Primary Key (`id PK`) e gli altri campi con i tipi relazionali (`string`, `int`).
2. **Il Diagramma delle Classi UML (Classe in RAM):** definisci la classe `Personaggio` con visibilità pubblica `+`, attributi tipizzati in stile Python (`id: int`, `nome: str`...) e le firme dei metodi.

### Parte 2 — Implementazione in Python (`student.py`)
Apri il file `student.py` e implementa:
1. La classe `Personaggio` con costruttore `__init__`, `self`, attributi, metodo `presentati()` e `__str__()`.
2. La funzione `main()` che:
	- Crea due eroi distinti: ad esempio Aragorn (id=1, livello=5) e Legolas (id=2, livello predefinito).
	- Stampa ciascun eroe con `print()` (verificando il funzionamento di `__str__`).
	- Stampa la presentazione di entrambi chiamando `presentati()`.

---

## 3. Esempio di Esecuzione del `main()`
```text
=== CREAZIONE EROI RPG ===
Personaggio #1: Aragorn (PV: 100/100)
Personaggio #2: Legolas (PV: 100/100)

Presentazione:
- Sono Aragorn, eroe di livello 5 con 100 PV.
- Sono Legolas, eroe di livello 1 con 100 PV.
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es01.py
```