# Esercizio 03: Relazione N:N di Dominio Reale — Studenti e Corsi tramite `Iscrizione`

> **Prerequisiti teorici**: Modulo 03 (Cap. 02 - Scomposizione ER di N:N e classi ponte)  
> **Obiettivo**: Modellare la relazione N:N tra Studenti e Corsi universitari/scolastici tramite l'entità ponte `Iscrizione`, gestendo la data e la verbalizzazione del voto d'esame.

---

## 1. Il Contesto di Business

Uno `Studente` si iscrive a molti `Corsi`, e un `Corso` ha molti `Studenti`. La classe ponte `Iscrizione` memorizza il `voto_esame` (inizialmente `None`).

### Criteri di Accettazione (Definition of Done)
- [ ] `Studente` ha `matricola: int`, `nome: str`.
- [ ] `Corso` ha `codice_corso: str`, `titolo: str`, `cfu: int`.
- [ ] `Iscrizione` ha `studente: Studente`, `corso: Corso`, `data_iscrizione: str`, `voto_esame: int | None = None`.
- [ ] Metodo `verbalizza_voto(voto: int) -> bool`:
  - Se `18 <= voto <= 30`: registra il voto in `self.voto_esame` e restituisce `True`.
  - Se il voto è fuori scala (< 18 o > 30): rifiuta e restituisce `False`.
- [ ] Metodo `is_superato() -> bool`:
  - Restituisce `True` se `voto_esame` è diverso da `None` e `>= 18`, altrimenti `False`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== GESTIONALE UNIVERSITA (RELAZIONE N:N) ===
Studente: Alice (Matricola 1001)
Corso: CS101 (Architettura Software, 6 CFU)

Iscrizione registrata in data: 2026-10-01
Stato esame iniziale: Superato? False (Voto: None)

Tentativo verbalizzazione voto 15 (insufficiente) -> Esito: False
Verbalizzazione voto 28 -> Esito: True
Stato finale esame: Superato? True (Voto: 28)
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es03.py
```
