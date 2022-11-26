import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()
miCursor.execute("""
    create table productos (
        id integer not null primary key autoincrement,
        nombre_Articulo varchar(50) unique not null,
        precio int not null,
        seccion varchar(50) not null)
""")

productos = [
    ("pelota", 20, "jugueteria"),
    ("pantalon", 20, "confeccion"),
    ("martillo", 25, "ferreteria"),
    ("jarron", 45, "ceramica"),
    ("pantalones", 35, "confeccion")
]
miCursor.executemany(
    "insert into productos values(NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()
