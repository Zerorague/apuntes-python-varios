import doctest
from pydoc import Doc


# def areaTriangulo(base, altura):
#     """calcula el area de un triangulo dado
#     >>> areaTriangulo(3,6)
#     9.0
#     """
#     return (base*altura)/2


# doctest.testmod()  # informa del error cuando existe en algun test


def compruebaMail(mailUsuario):
    """ la funcion compruebaMail, evalua un mail recibido en busca de la @, si tiene una aaroba es correcto, pero si tiene mas de una es incorrdcto.
    si la @ esta al final es incorrecto
    >>> compruebaMail('JulioASMB@gmail.com')
    True
    >>> compruebaMail('JulioASMBgmail.com')
    False
    >>> compruebaMail('JulioASMB@@gmail.com')
    False
    >>> compruebaMail('JulioASMBgmail.com@')
    False
    >>> compruebaMail('@JulioASMBgmail.com')
    False
    >>> compruebaMail('@')
    False

    """
    arroba = mailUsuario.count('@')
    if arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@') == 0:
        return False
    else:
        return True


doctest.testmod()
