class coche():
    def __init__(self) -> None:
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        if self.chequeo_interno():
            self.__enmarcha = arrancamos
            if self.__enmarcha:
                return "El coche esta en marcha"
            else:
                return "El coche esta parado"
        else:
            return "hay problemas para, no se puede hacer contacto"

    def estado(self):
        valor = self.__enmarcha

        print(
            f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} cm y un largo de {self.__largoChasis} cm. Ademas {self.arrancar(valor)}")

    def chequeo_interno(self):
        print("Ejecutando programa de chequeo...")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "ok"):
            return True
        else:
            return False


micoche = coche()
micoche.arrancar(0)
micoche2 = coche()
micoche2.arrancar(1)
# polimorfismo

objeto = micoche2

objeto.estado()
