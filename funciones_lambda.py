# que son
# funciones anonimas que se utilizan para abreviar

"""def areaTriangulo(base, altura):
    return (base*altura)/2


print(areaTriangulo(5, 7))
print(areaTriangulo(9, 6))"""


def area_triangulo(base, altura): return (base*altura)/2


area_triangulo(5, 2)


# pow es para elevar una base a un exponente
def al_cubo(numero): return print(pow(numero, 3))


al_cubo(13)


# para fomratear

def destacar_valor(comision): return print(f"¡${comision}!")


destacar_valor(1500)


def mul_11():

    for i in list(range(0, 11)):
        yield (i*11)


objeto = mul_11()

print(next(objeto))
print(next(objeto))
print(next(objeto))
print(next(objeto))
