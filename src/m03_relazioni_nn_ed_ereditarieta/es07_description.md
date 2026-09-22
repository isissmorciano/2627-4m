# Esercizio 07: Pipeline Completa — N:N ed Ereditarietà da Requisito Grezzo

> **Prerequisiti teorici**: Modulo 03 (Tutti i capitoli)  
> **Obiettivo**: Eseguire l'intera pipeline senza scaffolding integrando sia l'Ereditarietà IS-A che la relazione N:N con tabella ponte.

---

## 1. Il Testo dei Requisiti del Committente

> *«Realizziamo una piattaforma di corsi online. Tutti gli utenti del sistema hanno un id, un nome e una email. Gli utenti si dividono in Docenti (che hanno una tariffa_oraria) e Studenti (che hanno un credito_disponibile in Euro).*  
> *Ogni Corso ha codice, titolo e prezzo_iscrizione. Uno studente può iscriversi a più corsi e un corso accoglie più studenti (N:N).*  
> *L'iscrizione ha successo solo se lo studente ha credito sufficiente per pagare il corso: in tal caso il costo viene scalato dal credito dello studente e viene creata la scheda Iscrizione (con data e stato 'Attivo'). Se il credito è insufficiente, l'iscrizione è respinta.»*

---

## 2. Consegna dell'Esercizio

Apri `es07_student.md` ed `es07_student.py` e percorri la catena senza aiuti:
1. Formalizza la User Story e i Criteri di Accettazione.
2. Disegna ER (con tabella ponte) e UML (con gerarchia `Utente` $\to$ `Studente` / `Docente` e classe `Iscrizione`).
3. Implementa le classi in Python con `super()` e la logica di iscrizione a pagamento.

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es07.py
```
