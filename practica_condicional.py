# edad=101

# if 100>=edad>=0: #concatenacion de operadores de coomparacion
# else:
#     print("incorrecta")

#concatenacion de operadores de coomparacion ejemploo

# sueldo_presidente=int(input("Ingrese sueldo correspondiente al cargo de presidente: $"))
# sueldo_vice=int(input("Ingrese sueldo correspondiente al cargo de vice-presidente: $"))
# sueldo_gerente=int(input("Ingrese sueldo correspondiente al cargo de gerente: $"))
# sueldo_obrero=int(input("Ingrese sueldo correspondiente al cargo de obrero: $"))

# if sueldo_presidente>sueldo_vice>sueldo_gerente>sueldo_obrero:
#     print("esta todo correcto")
# else:
#     print("hay algo raro")


#operador in

print("Asignaturas optativas año 2021")
asi=("informatica grafica","sexologia","informatica aplicada a gis")
print(asi)
opcion=input("escribe la asignatura escogida: ")
asignatura=opcion.lower()



if asignatura in asi:
    print(f"Asignatura elegida {asignatura}")
else:
    print("Asignatura no existe")

print("comprobacion correo")

correo=input("ingrese su correo: ")
validacion=False

for i in correo:
    if i=="@":
        validacion=True


if validacion:
    print("correo validado")
else:
    print("correo invalido")
