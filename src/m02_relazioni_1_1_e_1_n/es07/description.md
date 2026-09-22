# Esercizio 07: Pipeline End-to-End da Requisito Grezzo — `Hotel` e `Stanze`

> **Prerequisiti teorici**: Modulo 02 (Tutti i capitoli)  
> **Obiettivo**: Eseguire l'intera pipeline di ingegneria del software da un testo informale su una relazione 1:N: Requisiti $\to$ US/CA $\to$ ER/UML $\to$ Sequenza $\to$ Dataclass $\to$ Pytest.

---

## 1. Il Testo dei Requisiti del Committente

> *«Gestiamo un piccolo hotel di charme. L'hotel ha un nome e gestisce un insieme di stanze (ciascuna con numero camera, tipo 'Singola'/'Doppia', prezzo e stato occupata/libera). Quando un ospite arriva, l'hotel deve poter assegnare la prima camera libera della tipologia richiesta impostandola come occupata. L'hotel deve poter calcolare il potenziale incasso totale a piena occupazione e contare quante camere sono attualmente libere.»*

---

## 2. Consegna dell'Esercizio

Apri `student.md` ed `student.py` e percorri la catena senza scaffolding:
1. Formalizza la User Story e i Criteri di Accettazione.
2. Disegna il modello ER (posizionando la FK sul lato Molti) e il Class Diagram UML.
3. Traccia il Diagramma di Sequenza della prenotazione con ricerca della stanza libera.
4. Implementa il codice Python con `@dataclass` e la funzione `main()`.

---

## 3. Verifica del Lavoro
```bash
pytest tests/test_m02_relazioni/test_es07.py
```
