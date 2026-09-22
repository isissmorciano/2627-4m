# Esercizio 02: Relazione 1-a-1 e Ciclo di Vita — Cartella Clinica e Paziente

> **Prerequisiti teorici**: Modulo 02 (Cap. 02 - Associazione 1-a-1 e gestione dello stato)  
> **Obiettivo**: Modellare e implementare una relazione 1:1 nel settore sanitario (`Paziente` e `CartellaClinica`), gestendo il ciclo di vita del legame (collegamento e scollegamento/dimissione senza riferimenti orfani).

---

## 1. Il Contesto di Business

In una clinica ospedaliera, ogni paziente ricoverato ha una specifica cartella clinica attiva.

> **User Story:**  
> *«Come Medico di reparto, voglio assegnare una Cartella Clinica a un Paziente ricoverato e poterla chiudere/scollegare alla dimissione, per garantire la tracciabilità delle cure senza lasciare record incoerenti.»*

### Criteri di Accettazione (Definition of Done)
- [ ] Il `Paziente` ha Primary Key `codice_fiscale: str` e `nome: str`.
- [ ] La `CartellaClinica` ha Primary Key `numero_cartella: int`, diagnosi (`diagnosi: str`) e FK `paziente_cf` (UNIQUE).
- [ ] Il metodo `assegna_cartella(cartella: CartellaClinica) -> bool`:
  - Se il paziente non ha cartella attiva: collega reciprocamente i due oggetti e restituisce `True`.
  - Se il paziente ha già una cartella: rifiuta l'assegnazione e restituisce `False`.
- [ ] Il metodo `dimetti() -> bool`:
  - Se ha una cartella attiva: imposta a `None` il riferimento reciproco in entrambi gli oggetti e restituisce `True`.
  - Se non aveva cartelle: restituisce `False`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== GESTIONALE CLINICA (RELAZIONE 1:1) ===
Paziente: Mario Rossi (CF: RSSMRA80A01H501U)
Cartella #501 (Diagnosi: Febbre persistente)

Assegnazione cartella -> Esito: True
Verifica: Mario Rossi ha la cartella #501
Verifica: La cartella #501 appartiene a Mario Rossi

Tentativo seconda assegnazione su stesso paziente -> Esito: False

Dimissione paziente -> Esito: True
Stato post dimissione:
- Paziente cartella: None
- Cartella proprietario: None
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es02.py
```
