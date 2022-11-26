import sqlite3
from tkinter import Variable

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

# variosProductos = [
#     ("camiseta", 10, "deportes"),
#     ("jarron", 90, "ceramica"),
#     ("camion", 20, "juguetes")
# ]

# miCursor.executemany("insert into productos values (?,?,?)", variosProductos)
miCursor.execute(
    "select * from productos order by precio desc limit 3 offset 1")
VariosProductos = miCursor.fetchall()

for product in VariosProductos:
    print(product)
miConexion.commit()

miConexion.close()
