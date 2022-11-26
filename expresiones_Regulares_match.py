

import re
nombre1 = "Jara Lopez"

nombre2 = "Antonio Gómez"

nombre3 = "Lara Lopez"

# re.IGNORECASE hace que ya no sea sensible a mayusculas o minusculas (casesensitive)
# . es comodin es decir la cadena puede empezar por cualquier caracter siempre y cuando le siga ara
if re.match(".ara", nombre3, re.IGNORECASE):
    print("hemos encontrado el nombre")
else:
    print("no lo hemos encontrado")
 # \d verifica si la cadena comienza por un digito
