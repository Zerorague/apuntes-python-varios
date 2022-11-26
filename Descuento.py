def Descuento(Precio, Descuento):
    return Precio + (Precio * (Descuento) / 100)


def Iva(Precio):
    return Precio * 1.19


def Cesta():
    Basket = {}
    total = []
    continuar = input("Agregar al carrito?(si/no): ")
    while continuar == "si":
        Precio = int(input("Ingrese precio: "))
        Descuentoo = int(input("Ingrese descuento (%): "))
        Basket[Precio] = Descuentoo
        continuar = input("Seguir comprando(si/no): ")
    for i in Basket:
        count = 0
        keyss = Basket.keys()
        i = i * Descuento(i, keyss[count] / 100)
        i = Iva(i)
        total.append(i)
        count += 1
    total = sum(total)
    return total


print(Cesta())
