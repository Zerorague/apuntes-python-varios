import random

def generador_random():
    numero=random.randint(0,100)
    return numero

generado=generador_random()
numero=int(input("ingrese su numero: "))

while numero!=generado:
    if numero<generado:
        print(f"el numero es mayor que {numero}")
        numero=int(input("ingrese su numero: "))
    elif numero > generado:
        print(f"el numero es menor que {numero}")
        numero=int(input("ingrese su numero: "))
   
print (f"Correcto! el numero era {generado} ")
