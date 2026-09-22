# Esercizio 05: Dominio E-Commerce — `Carrello` ed `ElementiCarrello` con Aggregazioni

> **Prerequisiti teorici**: Modulo 02 (Cap. 03 - 1:N e metodi di aggregazione)  
> **Obiettivo**: Modellare la relazione 1:N tra Carrello ed Elementi, implementando metodi di calcolo aggregato (totale carrello) e rimozione sicura.

---

## 1. Il Contesto di Business

In uno store online, ogni cliente ha un `Carrello` che contiene molti `ElementoCarrello` (ciascuno con nome prodotto, quantita e prezzo unitario).

### Criteri di Accettazione (Definition of Done)
- [ ] `ElementoCarrello` ha `id_prodotto: int`, `nome: str`, `quantita: int`, `prezzo_unitario: float`. Metodo `subtotale() -> float` (`quantita * prezzo_unitario`).
- [ ] `Carrello` memorizza `elementi: list[ElementoCarrello] = field(default_factory=list)`.
- [ ] `aggiungi_elemento(elemento: ElementoCarrello) -> None`: aggiunge l'elemento alla lista.
- [ ] `calcola_totale() -> float`: restituisce la somma dei subtotali di tutti gli elementi, arrotondata a 2 decimali.
- [ ] `rimuovi_prodotto(id_prodotto: int) -> bool`: se il prodotto è presente nel carrello lo rimuove e restituisce `True`, altrimenti `False`.

---

## 2. Esempio di Esecuzione del `main()`
```text
=== E-COMMERCE: CARRELLO SPESA (1:N) ===
Aggiunto: Mouse (2 x 25.00€)
Aggiunto: Tastiera (1 x 70.00€)
Totale carrello: 120.00€

Rimozione Mouse (id=101) -> Esito: True
Nuovo totale carrello: 70.00€
```

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es05.py
```
