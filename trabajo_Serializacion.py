import pickle

from numpy import MAY_SHARE_EXACT
# -------------------volcado de datos

listanombre = ["pedro", "juan", "julioop", "karina", "felipe"]

fichero_binario = open("texto_prueba.txt", "wb")

# argumentos/dato a volcar, fichero con el archivo
pickle.dump(listanombre, fichero_binario)

fichero_binario.close()
del fichero_binario


# recuperacion de datos

fichero_binario = open("texto_prueba.txt", "rb")

lista = pickle.load(fichero_binario)

fichero_binario.close()
del fichero_binario
print(lista)

# codificacion binaria objetos


class vehiculo():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        print(
            f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enmarcha}")


coche1 = vehiculo("Mazda", "MX5")
coche2 = vehiculo("Seat", "Leon")
coche3 = vehiculo("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("loscoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del fichero

# rescatar informacion serializada

fichero = open("loscoches", "rb")
Miscoches = pickle.load(fichero)
fichero.close()

for i in Miscoches:
    print("---------------")
    i.estado()
