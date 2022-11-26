

import re

lista_nombres = ["Ma1", "Se1", "Ma2", "Ba1", "Ma3", "Va1", "Va2", "Ma4"]

for ele in lista_nombres:
    if re.findall("^Ma[^0-3]$", ele):  # rango , $que termina entre un rango de o y t
        # el circunflejo es para negar el rango es decir me devolvera los que comienzan con Ma y lo que esta fuera del rango (Ma4)
        print(ele)
