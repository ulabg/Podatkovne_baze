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

Dodajo tri nove stranke: Erik, Fani in Gala.
```sql
INSERT INTO stranka 
(ime)
VALUES ('Erik'),('Fani'),('Gala');
```

Popravijo status naročila z id 3 na na poti.
```sql
UPDATE narocilo
SET status = 'na poti'
WHERE id = 3;
```

Dodajo novo naročilo, ki ga je ustvarila Gala za 200 enot izdelka. Id stranke za vstavljanje naročila pridobi avtomatsko. Status naročila naj bo v obdelavi.
```sql
INSERT INTO narocilo
VALUES (200,(SELECT id FROM stranka WHERE ime = 'Gala'),'v obdelavi');
```

Izbrišejo Alenko in vsa njena naročila.
```sql
DELETE FROM narocilo
WHERE id = (SELECT id FROM stranka WHERE ime='Alenka');
```

Ustvarijo novo naročilo za vse stranke, ki še niso oddale naročila. Količina naj bo stokratnik id stranke. Status naročila naj bo nastavljen na privzeto vrednost (oddano).
```sql

```

Zaključim vsa naročila, ki so na poti.
```sql

```