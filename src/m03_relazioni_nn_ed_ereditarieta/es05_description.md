# Esercizio 05: Override dei Metodi e Polimorfismo Dinamico

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Override e Polimorfismo in Azione)  
> **Obiettivo**: Implementare l'override del metodo `attacca(bersaglio)` nelle classi figlie e dimostrare il polimorfismo dinamico ciclando su una lista eterogenea di oggetti.

---

## 1. Il Contesto di Business

Tutti gli eroi possono attaccare, ma ciascuno lo fa secondo la propria natura:
* `Personaggio` base infligge un danno fisso di 10 PV.
* `Guerriero` fa l'**override**: calcola `danno = 10 + self.forza`.
* `Mago` fa l'**override**: se ha almeno 15 mana, consuma 15 mana e infligge 25 danni magici; altrimenti infligge 0 danni.

### Criteri di Accettazione (Definition of Done)
- [ ] Il metodo `attacca(bersaglio: Personaggio) -> str` della superclasse applica 10 danni al bersaglio.
- [ ] Nel `Guerriero`, l'override applica `10 + forza` danni al bersaglio e restituisce il messaggio con icona ⚔️.
- [ ] Nel `Mago`, l'override applica 25 danni se `mana >= 15` (riducendo il mana di 15) con icona ✨. Se mana insufficiente non applica danni e restituisce avviso.
- [ ] I punti vita del bersaglio non scendono mai sotto zero.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== SIMULAZIONE POLIMORFISMO IN BATTAGLIA ===
Bersaglio: Orco (PV: 100)

Turno della squadra polimorfica:
- ⚔️ Conan sferra un colpo potente da 25 danni su Orco!
- ✨ Merlino lancia un dardo magico da 25 danni (Mana rimasto: 35)!

Stato finale Orco: PV 50/100
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es05.py
```
