import pickle as pepi


class Vehiculo():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def __str__(self) -> str:
        return f"Vehiculo Registrado\nMarca:{self.marca}\nModelo:{self.modelo}"

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca:{self.marca}\nModelo:{self.modelo}\nEn marcha:{self.enmarcha}\nAcelerando:{self.acelera}\nFrenando:{self.frena}")


auto1 = Vehiculo("Mazda", "MX5")
auto2 = Vehiculo("Seat", "Leon")
auto3 = Vehiculo("Renault", "Megane")

autos = [auto1, auto2, auto3]

fichero = open("Coleccion vehiculos obj", "wb")
pepi.dump(autos, fichero)
fichero.close()
del fichero

fichero = open("Coleccion vehiculos obj", "rb")

lista_rescatada_objetos = pepi.load(fichero)
fichero.close()
del fichero

for i in lista_rescatada_objetos:
    i.estado()
