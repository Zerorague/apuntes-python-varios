import pickle

# lista = ["Felipe", "Cristofer", "Jose", "Agustin", "Isabel"]

# fichero = open("Lista_Nombres", "wb")

# pickle.dump(lista, fichero)

# fichero.close

# del fichero

fichero_Externo = open("lista_nombres", "rb")

lectura = pickle.load(fichero_Externo)

fichero_Externo.close()

print(lectura)
