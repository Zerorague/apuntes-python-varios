import sqlite3
con = sqlite3.connect("GestionProductos")
cur = con.cursor()

(cur.execute("SELECT * FROM productos"))
# (cur.execute("UPDATE productos SET precio=85 WHERE id=4"))
#(cur.execute("DELETE FROM productos WHERE id=5"))
consuta = cur.fetchall()
for i in consuta:
    print(i)

con.commit()
con.close()
