from io import open

from matplotlib.style import use


class User():
    def __init__(self, id, userName, passWord) -> None:
        self.__id = id
        self.__userName = userName
        self.__passWord = passWord

    @property
    def getId(self):
        return self.__id

    @property
    def getUserName(self):
        return self.__userName

    @property
    def getPassWord(self):
        return self.__passWord

    @getUserName.setter
    def setUserName(self, value):
        if value.isalnum():
            self.__userName = value

    @getPassWord.setter
    def setPassWord(self, value):
        if value.isalnum():
            self.__passWord = value


class Diario(User):
    def __init__(self, id, userName, passWord, titulo) -> None:
        super().__init__(id, userName, passWord)
        self.__titulo = titulo

    @property
    def getTitulo(self):
        return self.__titulo

    @getTitulo.setter
    def setTitulo(self, value):
        if value.isalnum():
            self.__titulo = value

    def documento(self, nombre_archivo, texto):
        documento = open(f"{nombre_archivo}.txt", "w")
        documento.write(
            f"{self.__titulo.capitalize().center(15)}\n{texto.center(10)}")
        documento.close()


Julio = User(1, "Julio", "a1234")

diario = Diario(1, Julio.getUserName, Julio.getPassWord, "Prueba 3")
diario.documento("esto es una prueba", "hola mundo hola mundo hola mundo")
diario.documento("esto es una prueba 3",
                 "hola mundo hola mundo hola mundo adios mundo")
