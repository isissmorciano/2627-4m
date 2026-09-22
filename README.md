# 2627-4m — Architettura e Modellazione Software

Repository degli esercizi di **Ingegneria del Software e Programmazione a Oggetti** per la classe 4ª (Indirizzo Informatica e Telecomunicazioni).

Il percorso adotta la metodologia professionale **Design-First**: il codice Python non è il punto di partenza, ma l'anello finale di una catena formale di analisi, modellazione e collaudo automatico.

---

## 🧭 La Catena Metodologica a 5 Stadi

Ogni problema viene affrontato attraversando rigorosamente 5 fasi sequenziali:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. REQUISITI & SPECIFICHE (User Story & Criteri di Accettazione)            │
│    Formulazione "Come [Attore] voglio [Azione] per [Scopo]"                 │
│    + Checklist delle regole di business e vincoli di confine.               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. MODELLAZIONE STATICA DEI DATI (ER vs UML in parallelo)                   │
│    - Tabella su disco (Diagramma ER con PK e Foreign Key)                   │
│    - Oggetto in memoria RAM (Class Diagram UML con visibilità e tipi)       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. MODELLAZIONE DINAMICA (Diagramma di Sequenza)                            │
│       Regola Aurea: ogni freccia in ingresso genera un metodo operativo     │
│       e definisce il principio di delega tra oggetti.                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. SVILUPPO PYTHON MODERNO (@dataclass)                                     │
│    Implementazione pulita con Type Hints, field(default_factory=list),      │
│    super().__init__(), override polimorfici e serializzazione JSON.         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. COLLAUDO AUTOMATICO (Pytest sui Criteri di Accettazione)                 │
│    Test deterministici a presidio di ogni singolo criterio e caso limite.   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Articolazione dei Moduli (44 Esercizi)

Il corso è organizzato in 7 moduli progressivi:

| Modulo | Cartella | Argomenti Chiave | N° Esercizi |
| :--- | :--- | :--- | :--- |
| **`m00`** | `src/m00_requisiti_e_user_stories/` | Requisiti informali, User Stories, Criteri di Accettazione, Edge Cases, Scomposizione Epic, Detective dei Requisiti. | **6** |
| **`m01`** | `src/m01_prima_entita_e_dataclass/` | Prima entità: Primary Key (PK), classi tradizionali con `__init__`/`self`, passaggio a `@dataclass`, metodi di stato, invarianti di salute/saldo/magazzino. | **8** |
| **`m02`** | `src/m02_relazioni_1_1_e_1_n/` | Due entità: Foreign Key (UNIQUE per 1:1, lato Molti per 1:N), Diagrammi di Sequenza, `default_factory=list`, Principio di Delega, aggregazioni carrello/scuola. | **8** |
| **`m03`** | `src/m03_relazioni_nn_ed_ereditarieta/` | Relazioni N:N con Entità di Raccordo (doppia FK e dati propri), Ereditarietà IS-A con `super()`, Override e Polimorfismo a runtime. | **8** |
| **`m04`** | `src/m04_persistenza_dati_json/` | RAM vs Disco: serializzazione con `asdict()`, deserializzazione e ricostruzione grafi di oggetti vivi, campo discriminatore polimorfico, test round-trip con `tmp_path`. | **4** |
| **`m05`** | `src/m05_architettura_c4_model/` | Visione di Sistema pre-progetto: C4 Livello 1 (System Context: utenti e API esterne) e Livello 2 (Container: Frontend, Backend Python, Database, Storage). | **6** |
| **`m06`** | `src/m06_progetti_sintesi_design_first/` | Progetti di sintesi completi in sottocartelle dedicate: 1 estensione guidata (RPG) + 3 tracce di business (Centro Sportivo, Flotta Veicoli, Corsi Palestra). | **4** |

---

## 📄 Struttura di un Esercizio

All'interno di ciascun modulo gli esercizi presentano una struttura standard:

- `esXX_description.md`: Capitolato del committente, User Story, Criteri di Accettazione, istruzioni ed **Esempio di Esecuzione del `main()`**.
- `esXX_student.md`: File di design in cui lo studente redige i diagrammi Mermaid (`erDiagram`, `classDiagram`, `sequenceDiagram`).
- `esXX_student.py`: Scheletro Python da implementare con docstring, metodi e funzione `main()`.
- `esXX_reference.md`: Soluzione modello del docente per i diagrammi Mermaid.
- `esXX_reference.py`: Soluzione modello del docente per il codice Python.

Nei progetti finali (`m06`), ogni cartella di progetto racchiude l'intera suite: `description.md`, `design_student.md`, `modello_student.py`, `gestore_student.py` e i rispettivi file `_reference`.

---

## 🛠️ Installazione e Setup dell'Ambiente

Il progetto richiede **Python 3.10+** e **Pytest**.

### 1. Clonazione e creazione ambiente virtuale
```bash
git clone https://github.com/<tua-organizzazione>/2627-4m.git
cd 2627-4m

python -m venv .venv

# Su Linux / macOS / WSL:
source .venv/bin/activate

# Su Windows (PowerShell / Git Bash):
.venv\Scripts\activate
```

### 2. Installazione dipendenze di qualità
```bash
pip install pytest ruff
```

---

## 🧪 Esecuzione dei Test di Collaudo

I test verificano che l'implementazione dello studente soddisfi rigorosamente i Criteri di Accettazione formalizzati.

### Test dello Studente (Cartelle `tests/test_mXX_*`)

* **Eseguire tutti i test di un intero modulo:**
  ```bash
  pytest tests/test_m01_entita
  pytest tests/test_m02_relazioni
  pytest tests/test_m03_espansione
  pytest tests/test_m04_persistenza
  pytest tests/test_m06_progetti
  ```

* **Eseguire i test di un singolo esercizio:**
  ```bash
  pytest tests/test_m01_entita/test_es01.py
  pytest tests/test_m02_relazioni/test_es04.py
  pytest tests/test_m06_progetti/test_p01.py
  ```

* **Eseguire tutti i test dello studente dell'intero anno:**
  ```bash
  pytest tests/test_m01_entita tests/test_m02_relazioni tests/test_m03_espansione tests/test_m04_persistenza tests/test_m06_progetti
  ```

---

### Test delle Soluzioni Docente (Cartelle `*_reference`)

I test reference verificano le soluzioni complete del docente (`esXX_reference.py`):

* **Eseguire i test reference di un modulo:**
  ```bash
  pytest tests/test_m01_entita_reference
  pytest tests/test_m02_relazioni_reference
  pytest tests/test_m03_espansione_reference
  pytest tests/test_m04_persistenza_reference
  pytest tests/test_m06_progetti_reference
  ```

* **Eseguire tutti i test reference dell'anno:**
  ```bash
  pytest tests/test_m01_entita_reference tests/test_m02_relazioni_reference tests/test_m03_espansione_reference tests/test_m04_persistenza_reference tests/test_m06_progetti_reference
  ```

---

## 🧹 Qualità e Stile del Codice (Ruff)

Prima di effettuare un commit, assicurarsi che il codice rispetti gli standard PEP 8 tramite **Ruff**:

```bash
# Analisi statica (linting):
ruff check .

# Formattazione automatica:
ruff format .
```

---

## 🎯 Regola Aurea del Detective di 4ª Anno
> *"Un diagramma non è una decorazione grafica e un test non serve a verificare la sintassi. Ogni diagramma ER mappa il database su disco, ogni freccia di sequenza genera un metodo in RAM, e ogni test Pytest collauda che una regola di business del committente sia inviolabile."*