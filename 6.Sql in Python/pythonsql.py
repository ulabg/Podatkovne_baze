import sqlite3

conn = sqlite3.connect('filmi.sqlite')
cur = conn.cursor()

#Izpišite podatke o filmu Marsovec.
poizvedba = """
SELECT id, naslov, dolzina, leto, ocena, oznaka
FROM film
WHERE naslov = 'Marsovec';
""" #""" pove da bomo delali več vrstic


rez = cur.execute(poizvedba).fetchone()
id_filma, naslov, dolzina, leto, ocena, oznaka = rez
print(f'{naslov} (id={id_filma}) {dolzina}min')


#Izpišite 20 najbolje ocenjenih filmov
poizvedba = """
SELECT naslov
FROM film
ORDER BY ocena
LIMIT 20;
"""
print(cur.execute(poizvedba).fetchall())
for naslov in cur.execute(poizvedba):
    print(naslov[0])

#Izpišite število filmov glede na oznako
poizvedba = """
SELECT oznaka, COUNT(*)
FROM film
GROUP BY oznaka;
"""
print(cur.execute(poizvedba).fetchall())
for oznaka, stevilo in cur.execute(poizvedba):
    print(f'{oznaka}:, {stevilo}')

# Izpišite režiserje filmov in njihove naslove, ki trajajo več kot 2 uri in pol
poizvedba = """
SELECT ime, naslov, dolzina
FROM film 
    JOIN vloga ON film.id = vloga.film
    JOIN oseba ON vloga.oseba = oseba.id
WHERE tip = 'R' AND dolzina > 150;
"""

print(cur.execute(poizvedba).fetchall())
for ime, naslov, dolzina in cur.execute(poizvedba):
    print(f'{ime}; {naslov}: ({dolzina} min)')

