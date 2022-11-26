import pickle

# volcado de datos↓
# lista_nombres = ["pedro", "ana", "maria", "isabel"]

# fichero_externo_binario = open("lista_nombres", "wb")  # "escritura binaria"

# pickle.dump(lista_nombres, fichero_externo_binario)

# fichero_externo_binario.close()

# del (fichero_externo_binario)

# rescate de datos↓

fichero = open("lista_nombres", "rb")

lista_nombres_recuperados = pickle.load(fichero)

print(lista_nombres_recuperados)
