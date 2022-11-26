from asyncore import read
import io

# archivo = io.open("archivo.txt", 'r')
# archivo.write("julio\njavier\njaviera\nkarina\nconi\n")
# archivo.close

archivo = io.open("archivo.txt", 'r')

lista = archivo.readlines()

archivo.close


a = input("su nombre: ")
a = a+"\n"
a = a.lower()
r = None
if a in lista and a == a in lista:
    print("puedes pasar")
else:
    print("no puedes pasar")
    r = input("registrar?(s/n)")
    if r == "s":
        key = input("password: ")
    else:
        pass

if r == "s" and key == "hcod":

    archivo = io.open("archivo.txt", "a")
    new_user = a
    archivo.write(new_user)
    archivo.close()
else:
    pass
