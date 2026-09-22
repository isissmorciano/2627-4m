# Esercizio 08: Detective di Classe — Review tra ER, UML e Codice Python

> **Prerequisiti teorici**: Modulo 01 (Tutti i capitoli) e Modulo 02 (Cap. 06 - Metodologia AI e Detective)  
> **Obiettivo**: Esercitare la revisione critica (Code & Model Review) scovando le discordanze e i difetti tra i Requisiti, il Modello ER, il Class Diagram UML e il codice Python, correggendo l'implementazione fino a renderla conforme.

---

## 1. Lo Scenario del Detective

Un programmatore junior (o un'intelligenza artificiale poco guidata) ha ricevuto il seguente requisito di business per un gestionale alberghiero:

> **Specifiche del Committente (`CameraHotel`):**  
> *«Ogni camera dell'albergo deve essere identificata in modo univoco dal suo numero (es. 101, 204). Dobbiamo registrare il tipo di camera ('Singola', 'Doppia', 'Suite'), la tariffa giornaliera in Euro e se la camera è attualmente occupata (inizialmente libera).*  
> *Le operazioni fondamentali sono:*  
> *1. `check_in()`: consentito solo se la camera è attualmente libera. Cambia lo stato in occupata e restituisce True. Se già occupata, rifiuta l'operazione e restituisce False.*  
> *2. `check_out()`: consentito solo se la camera è attualmente occupata. Libera la stanza e restituisce True. Se era già libera, rifiuta l'operazione e restituisce False.*  
> *3. `applica_sconto(percentuale: float)`: la direzione consente sconti promozionali solo tra l'1% e il 50% (0 < percentuale <= 50.0). Se la percentuale è valida, riduce la tariffa e restituisce True. Sconti > 50% o non positivi devono essere rifiutati lasciando la tariffa intatta e restituendo False.»*

---

## 2. I Documenti Difettosi Prodotti dal Collega

Nel file `student.md` troverai i modelli ER e UML proposti dal collega, e nel file `student.py` il suo codice.
Tuttavia, contengono **3 difetti gravi**:
* Un errore di integrità relazionale nel Modello ER.
* Una discordanza di visibilità e tipo di ritorno nel Diagramma UML.
* Due violazioni di invarianti nel codice Python (check-in cieco senza controllo occupazione e applicazione di sconti fuori limite senza protezione).

---

## 3. Consegna dell'Esercizio

### Parte 1 — Il Verdetto del Detective e i Modelli Corretti (`student.md`)
1. Compila il **Verdetto del Detective** spiegando con precisione i 3 errori individuati.
2. Riscrivi i diagrammi **ER** e **UML** corretti in sintassi Mermaid.

### Parte 2 — Correzione del Codice Python (`student.py`)
1. Correggi i metodi della classe `@dataclass CameraHotel` affinché rispettino rigorosamente i requisiti e gli invarianti.
2. Completa la funzione `main()` dimostrando che la classe corretta rifiuta check-in duplicati e sconti superiori al 50%.

---

## 4. Esempio di Esecuzione del `main()` Corretto
```text
=== TEST DIRETTO CAMERA HOTEL CORRETTA ===
Camera 101 (Doppia) | Tariffa: 120.00€ | Occupata: False

Primo check-in -> Esito: True (Stanza assegnata)
Secondo check-in consecutivo (errore) -> Esito: False (Stanza gia occupata!)

Tentativo sconto 70% (fuori policy > 50%) -> Esito: False
Tariffa inalterata: 120.00€

Applicazione sconto consentito 20% -> Esito: True
Nuova tariffa scontata: 96.00€

Check-out -> Esito: True (Stanza liberata)
```

---

## 5. Verifica del Lavoro
Lancia la suite di collaudo:
```bash
pytest tests/test_m01_entita/test_es08.py
```
