# son para especificar el estado inicial de una clase


class Perro:
    def __init__(self) -> None:
        self.__nombre = "bobby"
        self.__patas = 4
        self.__cola = 1
        self.__cabeza = 1
        self.__orejas = 2
        self.__ojos = 2
        self.__acostado = True

    @property
    def patas(self) -> int:
        return self.__patas

    @property
    def acostado(self) -> bool:
        return self.__acostado

    @property
    def nombre(self) -> str:
        return self.__nombre

    @patas.setter
    def patas(self, valor):
        self.patas = valor

    @nombre.setter
    def nombre(self, valor):
        self.nombre = valor

    @acostado.setter
    def acostado(self, valor):
        self.acostado = valor

    def setEstado(self, valor):
        self.__acostado = valor

    def setPatas(self, valor):
        if 0 <= valor <= 4:
            self.__patas = valor
        else:
            self.__patas = "los perros tienen entre 0 y 4 patas"

    def setNombre(self, valor):
        self.__nombre = valor

    def caracteristicas(self):
        if self.__acostado:
            print(
                f"{self.__nombre} tiene:\n{self.__patas} patas\n{self.__cola} cola\n{self.__cabeza} cabeza\n{self.__orejas} orejas\n{self.__ojos} ojos y esta acostado"
            )
        else:
            print(
                f"{self.__nombre} tiene:\n{self.__patas} patas\n{self.__cola} cola\n{self.__cabeza} cabeza\n{self.__orejas} orejas\n{self.__ojos} ojos y esta parado"
            )
