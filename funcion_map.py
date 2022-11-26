# aplica una funcion a cada elemento de una lista iterable, devolviendo una lista con resultados

class empleado():
    def __init__(self, nombre, cargo, salario) -> None:
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return f"{self.nombre} que trabaja como {self.cargo} y tiene un salario de ${self.salario}"


lista_empleados = [
    empleado("Juan", "Director", 15000),
    empleado("Julio", "Topografo", 30000),
    empleado("Felipe", "Informatico", 5000),
    empleado("ana", "Topografa", 8000),
    empleado("jose", "Informatico", 50000),
]


def calculo_comision(empleado):
    if empleado.salario < 6000:
        empleado.salario = empleado.salario*1.3
    return empleado


lista_empleados_comision = map(calculo_comision, lista_empleados)

for i in lista_empleados_comision:
    print(i)
