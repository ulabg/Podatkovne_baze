# ZDRUŽEVANJE

```sql
SELECT stolpci, MIN(stolpec1), MAX(stolpec2), AVG(stolpec3)
FROM tabela
ORDER BY urejevalni_pogoj
```
```sql
--Povprečna ocena filmov iz leta 2000
SELECT AVG(ocena)
FROM filmi
WHERE leto = 2000;

--Povprecna ocena filmov za vsako leto
SELECT leto, AVG(ocena)
FROM filmi
GROUP BY leto;

--Povprecna ocena filmov za vsako leto, ko je bilo vsaj 5 filmov
SELECT leto, AVG(ocena) AS povp_ocena, COUNT(*) AS st_filmov
FROM filmi
GROUP BY leto
HAVING st_filmov > 5;
```