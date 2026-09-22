# Esercizio 01: Relazione 1-a-1 — Foreign Key UNIQUE, Sequenza e Link Reciproco

> **Prerequisiti teorici**: Modulo 02 (Cap. 02 - L'Associazione 1-a-1: Dall'ER alla Sequenza al Codice)  
> **Obiettivo**: Modellare e implementare una relazione Uno-a-Uno (1:1) gestendo la Foreign Key con vincolo UNIQUE nel modello ER, tracciando il Diagramma di Sequenza per ricavare i metodi operativi e collegando reciprocamente le due istanze in Python.

---

## 1. Il Contesto di Business

Nel nostro videogioco RPG, ogni eroe deve poter equipaggiare uno zaino/inventario personale.

> **User Story:**  
> *«Come Giocatore, voglio assegnare uno specifico Zaino al mio Personaggio, in modo che l'Eroe abbia uno spazio dedicato per l'inventario e lo Zaino riconosca il suo legittimo proprietario.»*

### Criteri di Accettazione (Definition of Done)
- [ ] Un `Personaggio` può possedere al massimo uno `Inventario`.
- [ ] Un `Inventario` appartiene a un solo `Personaggio`.
- [ ] Alla creazione, l'eroe non ha zaino (`inventario = None`) e lo zaino non ha proprietario (`proprietario = None`).
- [ ] Il metodo `assegna_inventario(inv: Inventario)` dell'Eroe:
  1. Memorizza lo zaino in `self.inventario`.
  2. Notifica lo zaino invocando `inv.imposta_proprietario(self)` (collegamento bidirezionale).
- [ ] Dopo l'assegnazione, il legame è navigabile in entrambe le direzioni: da eroe a zaino (`eroe.inventario`) e da zaino a eroe (`zaino.proprietario`).

---

## 2. Consegna dell'Esercizio

### Parte 1 — Modellazione Statica e Dinamica (`es01_student.md`)
1. **Modello ER:** Definisci la tabella `PERSONAGGIO` e la tabella `INVENTARIO`, posizionando la Foreign Key `personaggio_id FK` nella tabella `INVENTARIO` con vincolo `UNIQUE` (relazione `||--||`).
2. **Diagramma di Sequenza:** Traccia l'interazione tra `Giocatore`, `Eroe: Personaggio` e `Zaino: Inventario` quando viene chiamato `assegna_inventario(zaino)`.
3. **Class Diagram UML:** Definisci le due classi con la relazione 1:1 e i metodi ricavati dalle frecce di sequenza (`assegna_inventario`, `imposta_proprietario`).

### Parte 2 — Implementazione in Python (`es01_student.py`)
1. Implementa le `@dataclass Inventario` e `Personaggio`.
2. Implementa i metodi di collegamento reciproco.
3. Nella funzione `main()`:
   - Crea un eroe (Aragorn, id=1) e uno zaino da 30 slot (id=101).
   - Mostra che prima dell'assegnazione i riferimenti sono `None`.
   - Esegui `eroe.assegna_inventario(zaino)` e dimostra la navigazione bidirezionale.

---

## 3. Esempio di Esecuzione del `main()`
```text
=== ASSEGNAZIONE RELAZIONE 1:1 ===
Stato iniziale:
- Eroe: Aragorn (Zaino: None)
- Zaino #101 (Proprietario: None)

Esecuzione: eroe.assegna_inventario(zaino)
Collegamento completato con successo!

Verifica navigazione bidirezionale:
- Da Eroe a Zaino: Aragorn possiede uno zaino da 30 slot.
- Da Zaino a Eroe: Lo zaino #101 appartiene a: Aragorn
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m02_relazioni/test_es01.py
```
