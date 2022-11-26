import numpy


def decorador_operaciones(funcion):
    def funcion_interna(*parametros):
        funcion(*parametros)
        print(
            f"el producto de los numeros es {numpy.product(parametros)}")
    return funcion_interna


@decorador_operaciones
def suma(*num):
    print(f"la suma es {sum(num)}")


suma(3, 4, 5)
