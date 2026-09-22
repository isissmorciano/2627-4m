# Esercizio 03: Metodi di Stato e Protezione degli Invarianti

> **Prerequisiti teorici**: Modulo 01 (Cap. 02 e Cap. 03 - Metodi che modificano lo stato ed invarianti di dominio)  
> **Obiettivo**: Modellare e implementare metodi operativi che modificano lo stato dell'oggetto proteggendo le regole di business (invarianti: nessun valore sotto zero, nessun overflow oltre il massimo).

---

## 1. Il Concetto di Invariante di Dominio

Nella programmazione a oggetti, un oggetto non è un semplice contenitore passivo di dati: è il **guardiano del proprio stato**.

Se lasciassimo che chiunque modificasse direttamente `eroe.punti_vita = -999`, l'oggetto entrerebbe in uno stato assurdo rispetto alle regole del gioco.

Un **invariante di dominio** è una regola di business che deve rimanere sempre vera durante tutto il ciclo di vita dell'oggetto.

### Le Regole del Nostro Dominio:
1. **Limite inferiore (Nessun punto vita negativo):** Se un colpo infligge più danni dei punti vita rimasti, i punti vita devono fermarsi esattamente a `0` (il personaggio è sconfitto, ma non ha vita negativa).
2. **Limite superiore (Nessun overflow):** Una pozione o magia curativa non può mai far salire i punti vita oltre la soglia massima `punti_vita_max` (fissata a 100).
3. **Controllo di validità dei valori:** Danni o cure con valori non positivi ($<= 0$) non devono alterare lo stato.
4. **Verifica della sopravvivenza:** Il metodo `is_vivo() -> bool` deve restituire `True` finché `punti_vita > 0`, e `False` quando `punti_vita == 0`.

---

## 2. Consegna dell'Esercizio

### Parte 1 — Modellazione Statica (`student.md`)
Apri `student.md` e crea da zero (lo scaffolding è ridotto):
1. **Diagramma ER:** L'entità `PERSONAGGIO` con Primary Key `id PK`, `nome string`, `livello int`, `punti_vita int`, `punti_vita_max int`.
2. **Class Diagram UML:** La classe `Personaggio` con i 5 attributi tipizzati e i metodi `subisci_danno(danno: int) void`, `cura(quantita: int) void`, `is_vivo() bool`.

### Parte 2 — Implementazione in Python (`student.py`)
Implementa la `@dataclass Personaggio`:
1. Definisci i campi con valori di default appropriati (`livello: int = 1`, `punti_vita: int = 100`, `punti_vita_max: int = 100`).
2. Implementa `subisci_danno(self, danno: int) -> None`: riduce i punti vita bloccandosi a 0 se il danno supera la vita residua.
3. Implementa `cura(self, quantita: int) -> None`: aumenta i punti vita bloccandosi a `punti_vita_max`.
4. Implementa `is_vivo(self) -> bool`.
5. Nella funzione `main()`, simula un ciclo di gioco:
   - Crea un eroe e visualizza lo stato iniziale.
   - Infliggi un danno parziale (es. 40) e mostra i PV rimasti.
   - Applica una cura superiore al necessario (es. 50) e dimostra che i PV si bloccano a 100.
   - Infliggi un danno mortale (es. 150), dimostra che i PV si bloccano a 0 e che `is_vivo()` restituisce `False`.

---

## 3. Esempio di Esecuzione del `main()`
```text
=== SIMULAZIONE COMBATTIMENTO ED INVARIANTI ===
Eroe creato: Conan (PV: 100/100, Vivo: True)

Conan subisce 40 danni!
PV attuali: 60/100

Conan beve una pozione da 50 PV!
PV attuali (bloccati al massimo): 100/100

Conan subisce un colpo critico da 150 danni!
PV attuali (bloccati a zero): 0/100
Stato eroe: Conan è sconfitto? True (is_vivo: False)
```

---

## 4. Verifica del Lavoro
Lancia il test automatico da terminale:
```bash
pytest tests/test_m01_entita/test_es03.py
```
