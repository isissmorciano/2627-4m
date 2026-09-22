# Esercizio 05: Scomposizione da Macro-Richiesta (Epic) a User Stories Atomiche

> **Prerequisiti teorici**: Modulo 00 (Cap. 03 - Dalle User Stories ai Requisiti)  
> **Obiettivo**: Imparare a prendere una macro-funzionalità (*Epic*) troppo complessa e spezzarla in User Stories atomiche, indipendenti e collaudabili, ciascuna con i propri Criteri di Accettazione.

---

## 1. Cos'è una Epic e perché va scomposta?

I clienti non parlano per singole storie utente: spesso esprimono bisogni complessi in un unico blocco:
> *"Vogliamo implementare l'intero modulo di recensioni per i prodotti del nostro e-commerce!"*

Una richiesta di questo tipo si chiama **Epic** (Macro-Requisito). È troppo vasta per essere modellata, sviluppata o testata in una volta sola:
* Coinvolge **attori diversi** (il cliente che compra, il visitatore che legge, il moderatore).
* Mescola **azioni indipendenti** (scrivere un commento, calcolare una media, approvare un testo).

Il compito dell'Ingegnere del Software è applicare il principio di **atomicità**: spezzare l'Epic in **User Stories indipendenti**, ognuna con il proprio valore concreto e i propri Criteri di Accettazione verificabili.

---

## 2. Il Testo dell'Epic del Committente

> *"Nel nostro portale e-commerce vogliamo introdurre il sistema di feedback. I clienti che hanno completato un acquisto devono poter lasciare un voto da 1 a 5 stelle e una recensione scritta. Gli altri visitatori devono poter leggere le recensioni e visualizzare il voto medio aggiornato della scheda prodotto. Infine, per evitare volgarità e spam, i moderatori della piattaforma devono poter revisionare le recensioni prima che diventino pubbliche."*

---

## 3. Consegna dell'Esercizio

Apri il file `es05_student.md` e scomponi l'Epic sovrastante in **3 User Stories atomiche distinte**, ciascuna corredata da almeno **2 Criteri di Accettazione**:

1. **US-01 (Scrittura del Feedback):** Dal punto di vista del cliente che rilascia la valutazione.
2. **US-02 (Consultazione e Sintesi):** Dal punto di vista del visitatore che consulta le recensioni e la media.
3. **US-03 (Moderazione dei Contenuti):** Dal punto di vista del moderatore che controlla e approva i testi.
