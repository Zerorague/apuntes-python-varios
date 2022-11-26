import pickle


class persona():
    def __init__(self, nombre, genero, edad) -> None:
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"se ha creado una persona nueva con el nombre de {self.nombre}")

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nGenero: {self.genero}\nEdad: {self.edad}"


class ListaPersonas():
    personas = []

    def __init__(self) -> None:

        listadepersonas = open(
            "ficheroexterno", "ab+")  # ab append binario
        listadepersonas.seek(0)
        try:
            # a self.personas (lista) se carga por pickle.load los archivos existentes en ficheroexterno
            self.personas = pickle.load(listadepersonas)
            print(f"se cargaron {len(self.personas)} personas")
        except:
            print("el fichero esta vacio")
        finally:
            listadepersonas.close()
            del listadepersonas

    def agregar(self, p):
        self.personas.append(p)
        self.guardar()

    def mostrar(self):

        for p in self.personas:
            print(p)

    def guardar(self):
        ListaPersonas = open("ficheroexterno", "wb")
        # donde esta la informacion/donde se volca la info
        pickle.dump(self.personas, ListaPersonas)
        ListaPersonas.close
        del ListaPersonas


milista = ListaPersonas()
milista.mostrar()

# print(perso)  # se muestra el metodo especial __str__ y no que es de tipo <__main__.persona object at 0x0000022E36B5BBB0>
