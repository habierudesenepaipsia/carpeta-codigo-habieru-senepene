import sqlite3

con = sqlite3.connect("problemasmixtoclasesegsemest.db")


cur = con.cursor()

cur.execute("create table if not exists persona(id integer, nombre text)")
data = [
    (1, "maria"),
    (2, "emiila"),
    (3, "valito")
]

for x in range(200,500000):
    data.append((x, "Nombre de X"))

cur.executemany("insert into persona values(?, ?)", data)
cur.execute("update persona set nombre = 'cambio' where id = 1")

con.commit()

con.close()

