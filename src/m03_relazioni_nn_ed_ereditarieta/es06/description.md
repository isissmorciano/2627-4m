# Esercizio 06: Polimorfismo di Business — Metodi di Pagamento E-Commerce

> **Prerequisiti teorici**: Modulo 03 (Cap. 03 - Polimorfismo applicato a sistemi reali)  
> **Obiettivo**: Modellare una gerarchia di pagamenti con metodo polimorfico `elabora_pagamento(importo)` specializzato per Carta di Credito (plafond) e Bonifico Bancario (commissione fissa).

---

## 1. Il Contesto di Business

In una cassa e-commerce, il carrello invoca un unico metodo `pagamento.elabora(totale)` senza dover conoscere i dettagli tecnici del singolo strumento.

### Criteri di Accettazione (Definition of Done)
- [ ] Classe base `MetodoPagamento` con metodo `elabora(importo: float) -> tuple[bool, str]`.
- [ ] `CartaCredito` estende con `plafond_residuo: float`.
  - Se `importo <= plafond_residuo`: scala l'importo e restituisce `(True, "Pagamento approvato con carta")`.
  - Altrimenti restituisce `(False, "Plafond carta insufficiente")`.
- [ ] `BonificoBancario` estende con `iban: str`, `commissione_fissa: float = 1.50`.
  - Addebita `importo + commissione_fissa` e restituisce sempre `(True, "Disposto bonifico di <totale>€ su IBAN <iban>")`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== CASSA E-COMMERCE: PAGAMENTI POLIMORFICI ===
Carrello da pagare: 100.00€

Tentativo 1 (Carta con 50€ plafond) -> Esito: False | Messaggio: Plafond carta insufficiente
Tentativo 2 (Carta con 200€ plafond) -> Esito: True | Messaggio: Pagamento approvato con carta
Tentativo 3 (Bonifico con 1.50€ comm.) -> Esito: True | Messaggio: Disposto bonifico di 101.50€ su IBAN IT88...
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m03_espansione/test_es06.py
```
