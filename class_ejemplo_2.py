class Perro():
    def __init__(self,nombre) -> str:
        self.__nombre= nombre

    
    @property
    def nombre(self)->str:
        return str(self.__nombre)
    
    @nombre.setter
    def nombre(self,valor) :
        self.__nombre=valor
    
    def bautizar(self,nuevo_nombre):
        self.nombre=nuevo_nombre
    
    def estado(self):
        print(f"el nombre del perro es {self.nombre}")

perro1=Perro(5)
perro1.estado()
perro1.bautizar(9)
perro1.estado()
    



