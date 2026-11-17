import sqlite3
from contextlib import closing


with closing(sqlite3.connect("problemasmixtoclasesegsemest.db")) as con:
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

    for registro in cur.execute("Select * from persona order by id desc"):
        print(registro(1))

    con.commit()

    con.close()

#import frontcontextlib
#import closing
#from contextlib import closing

#https://www.techonthenet.com/sqlite/index.php
#tutoriales de SQLite

#Tablas 

#SQLite viewer extension para revisar tablas