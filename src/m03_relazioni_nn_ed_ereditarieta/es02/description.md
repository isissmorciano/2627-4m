# Esercizio 02: Logica di Business sul Legame N:N — Danno Scalabile e Consumo Mana

> **Prerequisiti teorici**: Modulo 03 (Cap. 02 - Attributi e metodi sull'entità di raccordo)  
> **Obiettivo**: Implementare metodi operativi all'interno dell'entità di raccordo che utilizzano le informazioni combinate di entrambe le entità collegate (calcolo del danno in base alla padronanza).

---

## 1. Il Contesto di Business

Quando un eroe usa un'abilità appresa, l'efficacia dipende dal suo livello di maestria:
$$\text{Danno Effettivo} = \text{Danno Base Abilità} \times \text{livello\_padronanza}$$

### Criteri di Accettazione (Definition of Done)
- [ ] `Abilita` possiede `id: int`, `nome_abilita: str`, `danno_base: int`, `costo_mana: int`.
- [ ] `AbilitaAppresa` possiede il metodo `calcola_potenza_effettiva() -> int`:
  - Restituisce `danno_base * livello_padronanza`.
- [ ] `AbilitaAppresa` possiede il metodo `esegui_colpo() -> str`:
  - Restituisce la formula descrittiva: `"<nome_eroe> usa <nome_abilita> (Liv. <padronanza>) infliggendo <danno> danni!"`

---

## 2. Esempio di Esecuzione del `main()`
```text
=== ESECUZIONE ABILITA APPRESA N:N ===
Abilita creata: Fulmine (Danno Base: 20, Costo: 15)

Link: Thor apprende Fulmine a livello 3
Potenza effettiva calcolata: 60 danni (20 base * liv. 3)
Azione eseguita: Thor usa Fulmine (Liv. 3) infliggendo 60 danni!
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es02.py
```
