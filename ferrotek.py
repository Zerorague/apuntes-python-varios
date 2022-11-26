class Trabajador():
    def __init__(self, nombre, categoria, sueldo_base) -> None:
        self.__nombre = nombre
        self.__categoria = categoria
        self.__sueldo_base = sueldo_base
        self.__horas_extra = 0
        self.__tardanza = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @property
    def horas_extra(self):
        return self.__horas_extra

    @property
    def tardanza(self):
        return self.__tardanza

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    @sueldo_base.setter
    def sueldo_base(self, valor):
        self.__sueldo_base = valor

    @nombre.setter
    def horas_extra(self, valor):
        self.__horas_extra = valor

    @tardanza.setter
    def tardanza(self, valor):
        self.__tardanza = valor


class Boleta(Trabajador):

