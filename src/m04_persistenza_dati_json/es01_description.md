# Esercizio 01: Persistenza Base — Da RAM a JSON con `asdict` e Ritorno

> **Prerequisiti teorici**: Modulo 04 (Cap. 02 - Dalla RAM al Disco: La Serializzazione in JSON)  
> **Obiettivo**: Comprendere il ciclo di vita della persistenza: trasformare un oggetto vivo in RAM in dizionario con `dataclasses.asdict()`, salvarlo su file `.json` e ricostruire l'oggetto vivo al riavvio con `**kwargs`.

---

## 1. Il Contesto di Business

Finora i nostri eroi sono vissuti solo nella memoria RAM: al termine dello script, tutti i progressi andavano persi.

> **User Story:**  
> *«Come Giocatore, voglio salvare lo stato del mio eroe su file JSON e ricaricarlo al riavvio, per riprendere la partita dal punto esatto in cui l'avevo interrotta.»*

### Criteri di Accettazione (Definition of Done)
- [ ] La funzione pura `salva_personaggio(eroe: Personaggio, percorso: str) -> None`:
  - Converte l'istanza `Personaggio` in dizionario tramite `asdict()`.
  - Scrive il dizionario su file JSON con formattazione leggibile (`indent=4`, `encoding="utf-8"`).
- [ ] La funzione pura `carica_personaggio(percorso: str) -> Personaggio`:
  - Legge il file JSON tramite `json.load()`.
  - Ricostruisce e restituisce una **nuova istanza viva** di `Personaggio` usando l'operatore di unpacking `**dati`.
- [ ] L'eroe ricaricato mantiene esattamente gli stessi valori di `id`, `nome`, `livello`, `punti_vita` e può continuare a usare i suoi metodi.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== CICLO DI PERSISTENZA JSON: SINGOLA ENTITA ===
Eroe prima del salvataggio: Aragorn (Livello: 5, PV: 80)
Salvataggio su 'salvataggio_eroe.json' completato!

--- Riavvio simulato: ricaricamento da disco ---
Eroe ricaricato con successo: Aragorn (Livello: 5, PV: 80)
Verifica metodi: Aragorn subisce 20 danni...
Nuovi PV: 60/100 (L'oggetto e' vivo e operativo in RAM!)
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m04_persistenza/test_es01.py
```
