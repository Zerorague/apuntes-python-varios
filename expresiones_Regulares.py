# son una secuencia de caracteres que forman un patron de busqueda

# para que sirven ↓

# para el trabajo y procesamiento de texto

# ejemplos:
# busca un texto que se ajusta a un formato determinado (correo electronico)
# buscar si existe o no una cadena de caracteres dentro de un texto
# contar el numero de coincidencias de un texto
# etc

import re

cadena = "Vamo a aprender expresiones regulares"

texto_buscar = "aprender"

if re.search(texto_buscar, cadena) is not None:
    print("he encontrado el texto")
else:
    print("no he encontrado un texto")
