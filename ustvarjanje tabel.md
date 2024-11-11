# USTVARJANJE TABEL

### 1.BAZA NAROCILA

1. Ustvari bazo naročil (npr. narocila.sqlite), ki smo jo uporabljali prejšnji teden na vajah. Baza bo imela tabeli stranka in narocilo z naslednjnimi stolpci:

stranka:
id - primarni ključ tabele
ime - besedilna vrednost
vrednost ne sme biti NULL

narocilo:
id - primarni ključ tabele
kolicina - številska vrednost
vrednost mora biti večja od 0
stranka - tuj ključ, tabelo povezuje s stolpcem id v tabeli stranka
vrednost ne sme biti NULL
status - besedilna vrednost, ki ji dolžino lahko omejimo na 10 znakov
vrednost mora biti eden izmed nizov oddano, v obdelavi, na poti, zaključeno
privzeta vrednost je oddano

```sql
CREATE TABLE stranka (
    id     integer    PRIMARY KEY,
    ime    text       NOT NULL
);     

CREATE TABLE narocilo (
    id        integer    PRIMARY KEY,
    kolicina  integer    CHECK (kolicina > 0),
    stranka   integer    REFERENCES stranka(id)    NOT NULL,
    status    varchar(10) CHECK(status IN ('oddano', 'v obdelavi', 'na poti', 'zaključeno')) DEFAULT 'oddano'
);
```

2. V bazo vstavi podatke

```sql
INSERT INTO stranka
(ime)
VALUES ('Alenka'), ('Branko'), ('Cvetka'), ('David');

INSERT INTO narocilo
(kolicina, stranka, status)
VALUES (500, 2, 'v obdelavi'),
       (300, 3, 'na poti'),
       (800, 1, 'v obdelavi'),
       (150, 1, 'oddano'),
       (400, 4, 'zaključeno'),
       (400, 1, 'na poti');
```

### 2.BAZA UČITELJI

