class Coche():
    def __init__(self) -> None:
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def __str__(self) -> str:
        return "esto es un vehiculo"

    def arrancar(self, arrancamos):

        self.__enMarcha = arrancamos
        if self.__enMarcha and self.__chequeoInterno():
            return "El coche esta en marcha, todo esta bien"
        else:
            return "el coche esta parado"

    def estado(self):
        print(
            f"El coche tiene {self.__ruedas}, un ancho de {self.__anchoChasis}m, y un largo de {self.__largoChasis}m.")

    def __chequeoInterno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche()
miCoche2 = Coche()


print(miCoche.arrancar(True))
print("-----------------------")
print(miCoche2.arrancar(False))
miCoche2.estado()
