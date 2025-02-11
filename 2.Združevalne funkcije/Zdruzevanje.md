# ZDRUŽEVANJE
Zapišite poizvedbe za sledeče zahteve na bazi filmov z eno tabelo:

```sql
SELECT stolpci, MIN(stolpec1), MAX(stolpec2), AVG(stolpec3)
FROM tabela
ORDER BY urejevalni_pogoj
```
Vrnite povprečno oceno filmov iz leta 2000, zaokroženo na 1 decimalko.
```sql
--Povprečna ocena filmov iz leta 2000
SELECT AVG(ocena)
FROM filmi
WHERE leto = 2000;

Vrnite število filmov in povprečno oceno filmov vsakega režiserja. Rezultat uredite od najbolj uspešnega (najvišja ocena) do najmanj uspešnega režiserja.
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