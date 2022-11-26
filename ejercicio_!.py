# Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

# El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
# El nombre de usuario debe ser alfanumérico.
# Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
# Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
# Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
# Nombre de usuario válido, retorna True.



def is_alfanum(user):
    user=str(user)
    if user.isalnum(): #metodo que devuelve si la cadena de texto es alpha numerico
        return True
    else:
        return False
        

def len_caracteres(user):
    if is_alfanum(user):
        user=str(user)
        return len(user)
    return False


def validar_num_caracterese(user):
    user=str(user)
    if len_caracteres(user)<6 or len_caracteres(user)>12:
        return False
    else:
        return True


def programa(user):
    if validar_num_caracterese(user)==False:
        return print("el usuario debe tener entre 6 y 12 caracteres")
        
    elif is_alfanum(user)==False:
        return print("El nombre de usuario puede contener solo letras y números")
    else:
        return True


user=input("ingrese su usuario: ")

print(programa(user))