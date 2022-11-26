print("Programa verificacion mayoria de edad")

def programa(edad):
    if edad<18 or edad>100:
        return("no puedes pasar")
    else:
        return("Puedes pasar")

edad=int(input("Ingrese su edad: "))

print(programa(edad))
