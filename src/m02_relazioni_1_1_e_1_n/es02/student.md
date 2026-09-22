# Design Esercizio 02: Paziente e Cartella Clinica (1:1)

## 1. Modello ER (Database su Disco)

```mermaid
erDiagram
    PAZIENTE ||--|| CARTELLA_CLINICA : associato_a

    PAZIENTE {
        string codice_fiscale PK
        string nome
    }
    CARTELLA_CLINICA {
        int numero_cartella PK
        string paziente_cf FK "UNIQUE"
        string diagnosi
    }
```

---

## 2. Diagramma delle Classi UML (RAM)

```mermaid
classDiagram
    %% Disegna qui Paziente e CartellaClinica con i metodi assegna_cartella e dimetti
```
