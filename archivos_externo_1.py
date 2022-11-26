from io import open

# cracion -> apertura -> manipulacion -> cerrar

archivo_texto = open("archivo.txt", "r")

# lee linea a linea y lo guarda en una lista
leerTexto = archivo_texto.readlines()

archivo_texto.close()

print(leerTexto[0])
