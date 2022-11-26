
class rectangulo():
    largo=float(input("Ingrese largo: "))
    ancho=float(input("Ingrese Ancho: "))

    def area(self):
        return self.largo * self.ancho
    def perimetro(self):
        return (self.largo*2)+(self.ancho*2)
    def resultado(self,r):
        r=str(r).lower()
        
        
        if r=="a" or r=="area":
            return(f"La superficie del rectangulo es {self.area()} m2")
        elif r=="p" or r=="perimetro":
            return(f"El perimetro del rectangulo es {self.perimetro()} m")
        elif r=="ambas":
            return(f"La superficie del rectangulo es {self.area()} m2\nEl perimetro del rectangulo es {self.perimetro()} m")
class cubo(rectangulo):
    pass


rec=rectangulo()
rec.perimetro()
rec.area()
r=input("perimetro, area o ambas: ")
print(rec.resultado(r))

list=[60,51]
print(chr(list))





    