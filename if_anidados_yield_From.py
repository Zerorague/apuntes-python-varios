# crear baraja de naipe español

from numpy import var


numeros = ["As", "Dos", "Tres", "Cuatro", "Cinco",
           "Seis", "Siete", "BARDO", "CABALLO", "REY"]

casta = ["ORO", "ESPADAS", "BASTO", "COPAS"]

BARAJA = []

for i in numeros:
    for j in casta:
        BARAJA.append((f"{i} de {j}"))
print(BARAJA)
