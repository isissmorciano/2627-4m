# Esercizio 08: Detective di Architettura — Errori su Ereditarietà e Relazioni N:N

> **Prerequisiti teorici**: Modulo 03 (Tutti i capitoli)  
> **Obiettivo**: Esercitare la revisione critica scovando tre errori tipici di design: dimenticanza di `super()`, HAS-A scambiato per IS-A ed ereditarietà usata in modo improprio.

---

## 1. Lo Scenario del Detective

Un programmatore ha scritto una gerarchia per un'applicazione di noleggio veicoli.  
Il codice contiene due difetti gravi:
1. **Dimenticanza di `super()`:** nel costruttore di `Furgone` ha riscritto manualmente i campi base senza invocare `super().__init__()`, rompendo il principio di estendibilità.
2. **HAS-A scambiato per IS-A:** ha fatto ereditare `Motore` da `Veicolo` (*"Un motore è un veicolo?" NO! Un veicolo HA un motore!*).

---

## 2. Consegna dell'Esercizio

Apri `es08_student.md` ed `es08_student.py`:
1. Compila il **Verdetto del Detective** spiegando i due errori.
2. Ristruttura il codice:
   - `Veicolo` classe base (`targa: str`, `marca: str`, `tariffa_base: float`).
   - `Furgone` eredita correttamente con `super()` e aggiunge `capacita_carico_kg: int`.
   - `Motore` è una classe autonoma (`cilindrata: int`, `tipo_carburante: str`) posseduta dal veicolo (relazione HAS-A di composizione/associazione).

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es08.py
```
