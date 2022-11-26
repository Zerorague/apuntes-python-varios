import doctest
import math


def raiz(lista):
    """
    La funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasados por parametros en otra lista.

    >>> lista=[]
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raiz(lista)
    [2.0, 3.0, 4.0]
    """
    return [math.sqrt(n) for n in lista]


#print(raiz([5, 25, 16, 36]))


doctest.testmod()
