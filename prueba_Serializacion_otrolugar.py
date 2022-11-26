
# import pickle
# from trabajo_Serializacion import vehiculo

# fichero = open("loscoches", "rb")
# Miscoches = pickle.load(fichero)
# fichero.close()

# for i in Miscoches:
#     print("---------------")
#     i.estado()
from tkinter import *
from tkinter import ttk
root = Tk()

frm = ttk.Frame(root, padding=10)
ttk.Label(frm, text="Hola karina").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
