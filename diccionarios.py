# # mi_diccionario={

# # "Alemania":"Berlin",
# # "Francia":"Paris",
# # "Chile":"Santiago",
# # "España":"Madrid"

# # }

# # print(mi_diccionario["Chile"]) #accedemos al valor  del diccionario a partir de la clave

# # print(mi_diccionario) #accedemos al diccionario entero

# # #como agregar mas elementos

# # mi_diccionario["Italia"]="Lisboa" #asi he agregado un elemento mas al diccionario
# # #pero es erroneo

# # print(mi_diccionario)

# # #como modificar el valor de la la clave italia
# # mi_diccionario["Italia"]="Roma"

# # print(mi_diccionario) #diccionario modificado

# # #en un diccionario jamas podran haber dos claves iguales.

# # #como eliminar un elemento del diccionario con el metodo del

# # del mi_diccionario["Francia"]

# # print(mi_diccionario)

# #como ocupar tuplas para asignar claves o valores

# mitupla=("España","Chile","Francia")
# mi_diccionario={
# mitupla[0]:"Madrid",
# mitupla[1]:"Santiago",
# mitupla[2]:"Paris"


# }
# print(mi_diccionario[mitupla[1]]) #otra forma de acceder al valor de una clave

# #como ocupar una tupla o lista para alamacenar muchos valores a una clave

# mi_diccionario={
# 23:"Jordan",
# "Nombre":"Michael",
# "Equipo":"Chicago",
# "Anillos":(1991,1992,1993,1996,1997,1998)
# }

# print(mi_diccionario["Equipo"])
# print(mi_diccionario["Anillos"])

#tambien podemos guardar un diccionario dentro de un diccionario

mi_diccionario={
23:"Jordan",
"Nombre":"Michael",
"Equipo":"Chicago",
"Anillos":{
    "Temporadas par":(1992,1996,1998),
    "Temporadas impar":(1991,1993,1997)

    }
}

#print(mi_diccionario["Equipo"])
#print(mi_diccionario["Anillos"])

#metodos: keys, values, len

print(mi_diccionario.keys()) #me devuelve las claves
print(mi_diccionario.values()) #me devuelve los valores
print(len(mi_diccionario)) #Retorna el numero de elementos del diccionario (4)
