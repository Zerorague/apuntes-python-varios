# funciones de orden superior
# nos permite usar la progrmacion funcional

# verifica que los elementos de una secuencia cumplen una condicion, devolviendo un iterador con aquellos elementos que si la cumplen


"""def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numero_par, numeros)))

#lo mismo ↓ que arriba pero mas corto ↑


def num_inpar_lambda(num): return num % 2 == 1


print(list(filter(num_inpar_lambda, numeros)))"""


class empleado():
    def __init__(self, nombre, cargo, salario) -> None:
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return f"{self.nombre} que trabaja como {self.cargo} y tiene un salario de ${self.salario}"


lista_empleados = [
    empleado("Juan", "Director", 1500000),
    empleado("Julio", "Topografo", 8000000),
    empleado("Felipe", "Informatico", 500000),
    empleado("ana", "Topografa", 800000),
    empleado("jose", "Informatico", 500000),
]

salarios_altos = list(filter(
    lambda empleado: empleado.cargo.find("Topograf") == 0, lista_empleados))

for i in salarios_altos:
    print(i)
