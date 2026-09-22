# Esercizio 05: Esercizio Doppio Zoom — Da System Context (L1) a Container (L2)

> **Prerequisiti teorici**: Modulo 00 (Cap. 02 - Il C4 Model come Google Maps)  
> **Obiettivo**: Esercitare la progressione di zoom architetturale sullo stesso identico sistema software (E-Commerce): produrre prima la vista aerea di contesto e poi esplodere i container interni.

---

## 1. Lo Scenario di Business

Un'azienda di abbigliamento sportivo (*UrbanSport*) rinnova il proprio sistema vendite:

> **Requisiti Globali:**  
> *«I clienti navigano e acquistano dal sito web. Gli addetti alla logistica usano un'applicazione gestionale interna per preparare i colli. Il sistema si interfaccia con il gateway bancario per i pagamenti e con l'API del corriere DHL per generare le lettere di vettura.*  
> *All'interno, il sistema è composto da un Frontend Web E-Commerce, un Gestionale Magazzino Web, un Backend Python centrale che coordina gli ordini e un Database Relazionale che custodisce catalogo e ordini.»*

---

## 2. Consegna dell'Esercizio

Apri `es05_student.md` e realizza entrambi i diagrammi:
1. **Fase 1 — Vista dallo Spazio (C4 L1 System Context):** Mostra solo Clienti, Magazzinieri, la scatola nera `UrbanSport`, e i sistemi esterni `Gateway Pagamenti` e `DHL API`.
2. **Fase 2 — Zoom sui Blocchi (C4 L2 Container):** Apri la scatola nera ed esplodi i 4 container interni con i relativi protocolli di comunicazione.