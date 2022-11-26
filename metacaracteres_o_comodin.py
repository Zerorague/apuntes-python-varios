# anclas y clases de caracteres

import re

lista_nombres = ['ana martin gomez', 'maria martin',
                 'sandra lopez', 'santiago martim']

for elemento in lista_nombres:
    if re.findall('marti[nm]$', elemento):  # ^empieza por $ termina por
        print(elemento)
