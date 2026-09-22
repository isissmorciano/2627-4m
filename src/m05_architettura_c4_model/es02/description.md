# Esercizio 02: C4 Model Livello 1 — System Context Multi-Attore (Food Delivery)

> **Prerequisiti teorici**: Modulo 00 (Cap. 02 - C4 Model System Context)  
> **Obiettivo**: Mappare un ecosistema con molteplici ruoli utente concorrenti e diversi servizi partner esterni.

---

## 1. Lo Scenario di Business

Una startup lancia un'applicazione di consegna cibo a domicilio (*QuickBite*):

> **Capitolato del Committente:**  
> *«La nostra piattaforma mette in comunicazione tre figure: i Clienti (che scelgono i piatti e ordinano), i Ristoratori (che gestiscono i menu e preparano gli ordini) e i Rider (che accettano le consegne e portano il cibo a destinazione).*  
> *Il nostro sistema centrale QuickBite si appoggia a tre servizi terzi:*  
> *1. PayPal per incassare dai clienti e accreditare i compensi.*  
> *2. Google Maps API per calcolare i percorsi stradali ottimali dei rider e mostrare la posizione in tempo reale.*  
> *3. Twilio SMS per inviare codici di verifica e avvisi urgenti di consegna avvenuta.»*

---

## 2. Consegna dell'Esercizio

Apri `student.md` e disegna il diagramma `flowchart LR`:
1. I 3 attori umani: `Cliente`, `Ristoratore`, `Rider`.
2. Il sistema centrale: `QuickBite`.
3. I 3 sistemi/API esterne: `PayPal`, `Google Maps API`, `Twilio SMS`.
4. Tutte le connessioni con etichette chiare che descrivono il flusso informativo.