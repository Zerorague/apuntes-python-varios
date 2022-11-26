
from tkinter import *
from tkinter import messagebox

import sqlite3


# ------------------------funciones---------------------
def conexionBBDD():
    miconexion = sqlite3.connect("usuarios")
    micursor = miconexion.cursor()
    try:
        micursor.execute("""
            CREATE TABLE IF NOT EXISTS DATOS_USUARIOS (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL,
                PASS VARCHAR(50) NOT NULL,
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                COMENTARIO VARCHAR(500)

            )
        
        """)
        messagebox.showinfo("BBDD", "Conexion exitosa")
    except:
        messagebox.showwarning("ATENCION!", "base de datos ya existe")
    miconexion.close()


def salir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
    if valor == "yes":
        root.destroy()
    else:
        pass


def borrarCampos():
    id.set("")
    nombres.set("")
    password.set("")
    apellido.set("")
    direccion.set("")
    textoComentario.delete(1.0, END)


def insertar():
    miconexion = sqlite3.connect("usuarios")
    micursor = miconexion.cursor()
    micursor.execute(f"""
        INSERT INTO DATOS_USUARIOS(NOMBRE, PASS, APELLIDO, DIRECCION, COMENTARIO) VALUES ('{nombres.get()}','{password.get()}','{apellido.get()}','{direccion.get()}','{textoComentario.get(1.0,END)}')
    """)
    miconexion.commit()
    miconexion.close()
    messagebox.showinfo("registro", "registro exitoso")


def leer():
    con = sqlite3.connect("usuarios")
    cur = con.cursor()
    nombre = cur.execute(
        f"SELECT * FROM DATOS_USUARIOS WHERE ID = '{id.get()}' ")
    datos = nombre.fetchall()
    nombres.set(datos[0][1])
    password.set(datos[0][2])
    apellido.set(datos[0][3])
    direccion.set(datos[0][4])
    textoComentario.delete(1.0, END)
    textoComentario.insert(1.0, datos[0][5])
    con.close()


# -------------------------------------------------------
root = Tk()
root.geometry("300x400")
root.resizable(0, 0)
barramenu = Menu(root)
root.config(menu=barramenu, width=300, height=400)
bbddMenu = Menu(barramenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salir)

borrarMenu = Menu(barramenu, tearoff=0)
borrarMenu.add_command(label="borrar campos", command=borrarCampos)

crudMenu = Menu(barramenu, tearoff=0)
crudMenu.add_command(label="crear", command=insertar)
crudMenu.add_command(label="leer", command=leer)
crudMenu.add_command(label="actualizar")
crudMenu.add_command(label="borrar")

ayudaMenu = Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="licencia")
ayudaMenu.add_command(label="acerca de...")

barramenu.add_cascade(label="BBDD", menu=bbddMenu)
barramenu.add_cascade(label="BORRAR", menu=borrarMenu)
barramenu.add_cascade(label="CRUD", menu=crudMenu)
barramenu.add_cascade(label="AYUDA", menu=ayudaMenu)

# -----------------comienzo de campos-----------------------

miFrame = Frame(root)
miFrame.pack()
id = StringVar()
nombres = StringVar()
password = StringVar()
apellido = StringVar()
direccion = StringVar()


cuadroId = Entry(miFrame, textvariable=id)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=nombres)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadropass = Entry(miFrame, textvariable=password)
cuadropass.grid(row=2, column=1, padx=10, pady=10)
cuadropass.config(show="*")

cuadroApellido = Entry(miFrame, textvariable=apellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=direccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

# ---barra de texto---

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)


# ------------label----------------

idLabel = Label(miFrame, text="id:")
idLabel.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

nombreLabel = Label(miFrame, text="nombre:")
nombreLabel.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

passLabel = Label(miFrame, text="pass:")
passLabel.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="apellido:")
apellidoLabel.grid(row=3, column=0, sticky="ew", padx=10, pady=10)

direccionLabel = Label(miFrame, text="direccion:")
direccionLabel.grid(row=4, column=0, sticky="ew", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="comentario:")
comentarioLabel.grid(row=5, column=0, sticky="ew", padx=10, pady=10)


# ------------------------frame inferior botones---------------

frameBotones = Frame(root)
frameBotones.pack()

botonCrear = Button(frameBotones, text="Create", command=insertar)
botonCrear.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

botonRead = Button(frameBotones, text="read")
botonRead.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

botonUpdate = Button(frameBotones, text="update")
botonUpdate.grid(row=0, column=2, sticky="ew", padx=10, pady=10)

botonDelete = Button(frameBotones, text="delete")
botonDelete.grid(row=0, column=3, sticky="ew", padx=10, pady=10)

root.mainloop()
