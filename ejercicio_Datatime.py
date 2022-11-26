import datetime

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
fecha = datetime.datetime.now()
year = fecha.strftime("%Y")

resultado = 100-edad + int(year)

print(resultado)
