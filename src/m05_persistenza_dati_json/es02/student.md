# Design Esercizio 02: Ricostruzione Collezioni 1:N

## Diagramma Concettuale di Ricostruzione

```text
File JSON (Dati serializzati)
  │
  ▼ json.load()
Dizionario con lista di dict grezzi: [{'id': 1, 'nome': 'Spada'}, ...]
  │
  ▼ [Oggetto(**d) for d in lista]
Lista di vere istanze in RAM: [Oggetto(id=1, nome='Spada'), ...]
  │
  ▼ Inventario(..., oggetti=lista_ricostruita)
Grafo di oggetti vivo e operativo al 100%!
```
