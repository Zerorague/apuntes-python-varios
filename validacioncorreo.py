print("validacion correo")

correo=input("Ingrese su correo: ")
email=correo.lower()

if ("@gmail" in email and ".com" in email) or ("@gmail" in email and ".cl" in email):
    print("correo valido")
else:
    print("correo invalido")
