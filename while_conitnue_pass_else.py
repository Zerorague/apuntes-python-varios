for letra in "python":

    if letra=="h": #en la iteracion cuando encuentra la letra h, ignora esa iteracion
        continue #conitnue
    print(f"viendo la letra {letra}")

#si quiero contrar cuantos caracteres tiene una palabra

print("Programa contador de letras")

count=-1

frase=input("ingrese frase o plabara a evaluar: ")

for i in frase:
    if frase==" ":
        continue
    count+=1
print(count)

#el pass es como para dejar un trabajo a medias