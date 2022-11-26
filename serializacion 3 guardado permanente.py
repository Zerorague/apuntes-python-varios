import pickle


class Persona():
    def __init__(self, nombre, genero, edad) -> None:
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"se ha creado una persona nueva con el nombre de {self.nombre}")

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nGenero: {self.genero}\nEdad: {self.edad}"


class listaPersonas():
    personas = []

    def __init__(self) -> None:
        listaDePersonas = open("ficheroExternoPersonas", "ab+")
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print(f"se cargaron {len(self.personas)} del fichero externo")
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del listaDePersonas

    def agregarPersona(self, *p):
        for i in p:
            self.personas.append(i)
            self.__guardarPersonas()

    def __guardarPersonas(self):
        listaPersonas = open("ficheroExternoPersonas", "wb")
        pickle.dump(self.personas, listaPersonas)
        listaPersonas.close()
        del listaPersonas

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)


miLista = listaPersonas()

miLista.mostrarPersonas()
