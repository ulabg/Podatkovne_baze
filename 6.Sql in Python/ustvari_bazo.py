import sqlite3

conn = sqlite3.connect('svet.sqlite')
kazalec = conn.cursor()

# tabele = ["drzava", "kontinent"]
# for tabela in tabele:
    # pobrisi_tabelo = f"DROP TABLE IF EXISTS {tabela}"
    # kazalec.execute(pobrisi_tabelo)

pobrisi_kontinent = 'DROP TABLE IF EXISTS kontinent'
pobrisi_drzava = 'DROP TABLE IF EXISTS drzava'
kazalec.execute(pobrisi_drzava)
kazalec.execute(pobrisi_kontinent)

ustvari_kontinent = """
CREATE TABLE kontinent ( 
    id INTEGER PRIMARY KEY,
    ime TEXT NOT NULL
);
"""
kazalec.execute(ustvari_kontinent)

ustvari_drzavo = """
CREATE TABLE drzava (
    id INTEGER PRIMARY KEY,
    ime TEXT NOT NULL,
    id_kontinenta INTEGER REFERENCES kontinent(id)
);
"""
kazalec.execute(ustvari_drzavo)

vstavi_evropo = """
INSERT INTO kontinent
(ime)
VALUES ('Evropa');

"""
kazalec.execute(vstavi_evropo)
conn.commit()
conn.close()


