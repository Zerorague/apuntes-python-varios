from serializacion_2_objetos import Vehiculo
import pickle as pepi

fichero = open("Coleccion vehiculos obj", "rb")

lista_rescatada_objetos = pepi.load(fichero)
fichero.close()
del fichero

for i in lista_rescatada_objetos:
    i.estado()
