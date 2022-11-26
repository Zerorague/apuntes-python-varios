from io import open


# manejo de cursor metodo seek()

archivo = open("archivo.txt", "r+")  # r+ es escritura y lectura

print(archivo.read())

archivo.seek(0)  # movemos el cursor

# no imprime nada por que el cursor debe posicionarse al principio ↑
# print(archivo.readlines())
lista_texto = archivo.readlines()
lista_texto[1] = "esta linea ha sido incluida desde el exterior \n"

archivo.seek(0)
archivo.writelines(lista_texto)  # para agregar informacion por listas
