

# def numpar(a): #funcion normal(return) de numeros pares
#     lista=[]
#     count=2
#     while count<=a:
#         if count%2==0:
#             lista.append(count)
#             count+=2 #me devuelve toda la lista
#     return lista


# # ahora con yield

# def numpares(a): #funcion normal(return) de numeros pares
#     count=2
#     while count<=a:
#         if count%2==0:
#             yield count #yield es producir, estamos produciendo un numero par
#             count+=2

# pares_gen=numpares(8) #guardarlo en una variable hace que se pueda guardar el numero generado en suspension

# #for i in pares_gen:
# #    print(i)

# print(next(pares_gen))
# print(next(pares_gen))
# print(next(pares_gen)) #el next crea un estado de suspensión
# print(next(pares_gen))


# def pares(x):
#     count=1
#     while count <=x:
#         if count%2==0:
#             yield count
#             count+=1
#         else:
#             count+=1
#             continue

# devuelve_pares=pares(3.151515)

# for i in devuelve_pares:
#     print(i)
