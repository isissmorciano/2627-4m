# Esercizio 04: C4 Model Livello 2 — Container Multi-Device con File Storage (App Palestra)

> **Prerequisiti teorici**: Modulo 00 (Cap. 02 - Container con client multipli e storage file)  
> **Obiettivo**: Modellare un'architettura con due interfacce utente eterogenee (Mobile App per atleti e Web Dashboard per istruttori) collegate allo stesso Backend con separazione tra dati tabellari (DB) e file multimediali (Storage).

---

## 1. Lo Scenario di Business

La catena fitness *FitLife* realizza una piattaforma digitale integrata:

> **Capitolato Tecnico:**  
> *«Gli iscritti usano un'App Mobile (iOS/Android) per timbrare l'ingresso al tornello e consultare la propria scheda esercizi.*  
> *I personal trainer usano una Web Dashboard da computer per creare le schede e caricare i video dimostrativi.*  
> *Entrambi i client comunicano via API HTTPS con un unico Backend Python che gestisce la logica di business.*  
> *I dati strutturati (utenti, scadenze, ingressi) sono salvati in un Database SQL; i file pesanti (PDF delle schede e video MP4 degli esercizi) sono archiviati su un Cloud File Storage separato.»*

---

## 2. Consegna dell'Esercizio

Apri `student.md` e disegna il Container Diagram:
1. Attori: `Iscritto Palestra` e `Personal Trainer`.
2. I due Frontend distinti: `App Mobile` e `Web Dashboard`.
3. Il `Backend API Python`.
4. I due archivi dati: `Database SQL` (per i record) e `File Storage` (per PDF e video).