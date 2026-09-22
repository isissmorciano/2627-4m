# Esercizio 06: Detective Architetturale — Riconoscere gli Errori di Livello nel C4

> **Prerequisiti teorici**: Modulo 00 (Cap. 02 - Confini e granularità nel C4 Model)  
> **Obiettivo**: Esercitare l'analisi critica individuando e correggendo i tre errori più gravi commessi nei diagrammi C4: confondere una classe con un container, posizionare il database fuori dal confine del sistema, e dimenticare i protocolli di comunicazione.

---

## 1. Lo Scenario del Detective

Un analista inesperto ha presentato un diagramma C4 Livello 2 che pretende di descrivere un sistema di prenotazione visite mediche.  
Il diagramma contiene **3 violazioni concettuali gravi**:
1. **Errore di granularità (Confusione Livello 2 con Livello 4):** Ha inserito un blocco chiamato `Classe Prenotazione` come se fosse un container! Le classi vivono dentro il codice, non sono applicazioni o archivi eseguibili autonomamente.
2. **Errore di confine (Boundary scorretto):** Ha disegnato il `Database Pazienti` all'esterno del sistema, trattandolo come se fosse un servizio terzo di un'altra azienda. Il database è invece il cuore protetto del sistema stesso.
3. **Mancanza di protocolli:** Le frecce non indicano come i blocchi dialogano (niente HTTPS, niente SQL), rendendo il diagramma vago e inutile per gli sviluppatori.

---

## 2. Consegna dell'Esercizio

Apri `es06_student.md`:
1. Compila il **Verdetto del Detective** spiegando con precisione i 3 errori individuati.
2. Ridisegna il diagramma **C4 Container Livello 2 corretto** in sintassi Mermaid.