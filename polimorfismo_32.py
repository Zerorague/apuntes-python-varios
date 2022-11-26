# Un objeto puede cambiar de forma dependiendo del contexto

class Coche():
    def desplazamiento(self):
        print("me desplazo utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("me desplazo usando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("me desplazo usando 6 ruedas")


def desplazamientovehiculo(vehiculo):  # funcion para polimorfismo
    vehiculo.desplazamiento()


miVehiculo = Moto()

desplazamientovehiculo(miVehiculo)
