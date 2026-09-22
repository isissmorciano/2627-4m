# Esercizio 01: Relazione Molti-a-Molti (N:N) — La Regola dell'Entità di Raccordo

> **Prerequisiti teorici**: Modulo 03 (Cap. 02 - Le Relazioni Molti-a-Molti e l'Entità di Raccordo)  
> **Obiettivo**: Comprendere perché una relazione N:N non può essere piatta, scomporla in due relazioni 1:N tramite un'Entità di Raccordo (`AbilitaAppresa`) con doppia Foreign Key in ER e implementare la classe ponte con attributi propri del legame in Python.

---

## 1. Il Contesto di Business

Nel nostro videogioco RPG, gli eroi possono apprendere diverse abilità magiche e tecniche:
* Un `Personaggio` può apprendere **molte** `Abilita`.
* Una stessa `Abilita` (es. *"Palla di Fuoco"*) può essere appresa da **molti** `Personaggi`.

> **User Story:**  
> *«Come Giocatore, voglio che il mio Personaggio possa apprendere diverse Abilità e migliorare la propria maestria, per affrontare sfide più difficili durante l'avventura.»*

### Criteri di Accettazione (Definition of Done)
- [ ] La relazione N:N è scomposta nella tabella/classe intermedia `AbilitaAppresa`.
- [ ] Nel modello ER, `ABILITA_APPRESA` possiede due Foreign Key: `personaggio_id FK` e `abilita_id FK`.
- [ ] L'entità di raccordo memorizza il dato proprio del legame: `livello_padronanza` (intero da 1 a 5, default 1).
- [ ] Il metodo `potenzia()` di `AbilitaAppresa` incrementa `livello_padronanza` di 1 fino al tetto massimo di 5. Oltre 5 il livello non aumenta.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== RELAZIONE MOLTI-A-MOLTI: EROI ED ABILITA ===
Eroi: Aragorn (id=1), Merlino (id=2)
Abilita create: Palla di Fuoco (id=10, Mana: 25)

Assegnazione N:N tramite AbilitaAppresa:
- Aragorn apprende Palla di Fuoco a livello 1
- Merlino apprende Palla di Fuoco a livello 3

Merlino si allena e potenzia l'abilita!
Nuovo livello padronanza Merlino: 4
Livello padronanza Aragorn (inalterato): 1
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es01.py
```
