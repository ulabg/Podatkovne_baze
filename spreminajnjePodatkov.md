# Spreminjanje 

## Vaje s tabelo naročil
Dana je enostavna baza naročil s tabelama stranka in naročilo: Dano imamo podatkovno bazo naročil s tabelama stranka in narocilo. Tabela stranka vsebuje IDje in imena strank, tabela narocilo pa IDje naročil, količino naročenih izdelkov, tuj ključ stranka, ki tabelo povezuje s tabelo stranka ter status naročila, ki ima lahko vrednost oddano, v obdelavi, na poti ali zaključeno.

Tabela stranka: 
```sql
SELECT id, ime FROM stranka
```
Tabela narocilo:
```sql
SELECT * FROM narocilo
```
```sql