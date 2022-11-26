import pickle


class vehiculo():
    def __init__(self, marca, modelo) -> None:
        self.__marca = marca
        self.__modelo = modelo
        print(f"se ha creado un vehiculo de marca {self.__marca}")

    def __str__(self) -> str:
        return f"Vehiculo marca {self.__marca}\nmodelo {self.__modelo}"


class listavehiculos():
    coches = []

    # cada vvez que se llame la clase se hara lo que esta dentro del constructor
    def __init__(self) -> None:
        listadecoches = open("ficheroexternovehiculos", "ab+")
        listadecoches.seek(0)  # mover el cursor al inicio del documento

        try:
            self.coches = pickle.load(listadecoches)

            print(
                f"se han cargado {len(self.coches)} vehiculos del dichero externo")
        except:
            print("el fichero esta vacio")
        finally:
            listadecoches.close()
            del listadecoches

    def agregar(self, vehiculo_obj):
        self.coches.append(vehiculo_obj)
        agregar_a_fichero_Externo = open("ficheroexternovehiculos", "wb")
        pickle.dump(self.coches, agregar_a_fichero_Externo)

    def mostrar(self):
        for i in self.coches:
            print(i)


auto = vehiculo("toyota", "yaris")
camioneta = vehiculo("mitsubishi", "L-200")

milista = listavehiculos()


milista.mostrar()
