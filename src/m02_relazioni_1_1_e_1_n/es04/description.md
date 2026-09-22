# Esercizio 04: Il Principio di Delega — `Eroe` delega a `Zaino`

> **Prerequisiti teorici**: Modulo 02 (Cap. 03 - Diagramma di Sequenza e Delega delle Responsabilità)  
> **Obiettivo**: Comprendere e implementare il principio di delega: un oggetto coordinatore (`Personaggio`) non manipola direttamente le collezioni interne del componente (`Inventario`), ma delega l'azione invocando i metodi del componente.

---

## 1. Il Contesto di Business

L'utente comanda l'eroe: `eroe.raccogli_oggetto(pozione)`. L'eroe, se ha uno zaino equipaggiato, delega l'inserimento allo zaino.

### Criteri di Accettazione (Definition of Done)
- [ ] Il metodo `raccogli_oggetto(ogg: Oggetto) -> bool` di `Personaggio`:
  - Se l'eroe non ha uno zaino (`inventario is None`): restituisce `False`.
  - Se l'eroe ha uno zaino: delega invocando `self.inventario.aggiungi_oggetto(ogg)` e ne restituisce l'esito booleano.
- [ ] Il metodo `rimuovi_oggetto_per_nome(nome: str) -> Oggetto | None` di `Inventario`:
  - Cerca l'oggetto nella lista per nome: se trovato, lo rimuove e lo restituisce.
  - Se non trovato, restituisce `None`.
- [ ] Il metodo `usa_oggetto(nome: str) -> bool` di `Personaggio`:
  - Delega allo zaino la rimozione dell'oggetto. Se presente restituisce `True`, altrimenti `False`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== PRINCIPIO DI DELEGA (EROE -> ZAINO) ===
Eroe senza zaino tenta raccolta -> Esito: False

Equipaggiamento zaino completato!
Eroe raccoglie Pozione -> Esito: True (delega riuscita)
Eroe raccoglie Spada -> Esito: True (delega riuscita)

Eroe usa Pozione -> Esito: True (oggetto rimosso dallo zaino)
Eroe tenta uso Scudo (non presente) -> Esito: False
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es04.py
```
