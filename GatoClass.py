from PerroClass import *


class Gato(Perro):
    def __init__(self) -> None:
        super().__init__()
        self.__bigotes = "si"

    @property
    def bigotes(self):
        return self.__bigotes

    @bigotes.setter
    def bigotes(self, valor):
        self.__bigotes = valor

    def bigote(self, valor):
        self.__bigotes = valor

    def caracteristicas(self):
        super().caracteristicas()
        print(f"bigotes: {self.__bigotes}")
