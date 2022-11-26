#ejercicio n°1
print("Programa maquina dispensadora de bebidas")
class Maquina():
    def _init_(self,stock_coca,stock_fanta,stock_sprite,precio) -> int:
        self.__stock_coca=stock_coca
        self.__stock_fanta=stock_fanta
        self.__stock_sprite=stock_sprite
        self.__precio=precio
        self.__recaudacion=0

    @property
    def stock_coca(self)-> int:
        return self.__stock_coca
    @property
    def stock_fanta(self)-> int:
        return self.__stock_fanta
    @property
    def stock_sprite(self)-> int:
        return self.__stock_sprite
    @property
    def precio(self)-> int:
        return self.__precio
    @property
    def recaudacion(self)->int:
        return self.__recaudacion
    
    
    @stock_coca.setter
    def stock_coca(self,valor):
        self.__stock_coca=valor
    @stock_fanta.setter
    def stock_coca(self,valor):
        self.__stock_fanta=valor
    @stock_sprite.setter
    def stock_sprite(self,valor):
        self.__stock_sprite=valor
    @precio.setter
    def precio(self,valor):
        self.__precio=valor
    @recaudacion.setter
    def recaudacion(self,valor):
        self.__recaudacion=valor
    
    def comprar_lata(self,nom_lata,monto):
        if monto<self.precio:
            return f"Faltan ${self.precio-monto} "
        if self.stock_coca>0 and nom_lata=="coca":
                self.stock_coca+=-1
                self.recaudacion+=self.precio
        elif self.stock_fanta>0 and nom_lata=="fanta":
                self.stock_fanta+=-1
                self.recaudacion+=self.precio
        elif self.stock_sprite>0 and nom_lata=="sprite":
                self.stock_sprite+=-1
                self.recaudacion+=self.precio
        else:
            return "no hay stock"
        
        return f"su vuelto es de ${monto-self.__precio}"

    def recarga(self,nom_lata,cantidad):
    
        if nom_lata=="coca":
            self.stock_coca+=cantidad
            return f"ha recargado {cantidad} lt de coca cola"
        if nom_lata=="fanta":
            self.stock_fanta+=cantidad
            return f"ha recargado {cantidad} lt de fanta"
        if nom_lata=="sprite":
            self.stock_sprite+=cantidad
            return f"ha recargado {cantidad} lt de sprite"

    def cambio_precio(self,nuevo_precio):
        self.precio=nuevo_precio
    
    def estado_maquina(self):
        print("------Estado Maquina-----")
        print(f"el precio de la lata es ${self.precio}")
        print(f"el stock de coca cola es {self.stock_coca} lt")
        print(f"el stock de fanta es {self.stock_fanta} lt")
        print(f"el stock de sprite es {self.stock_sprite} lt")
        print(f"se han recaudado ${self.recaudacion}")

maquina=Maquina(3,3,3,500)

print(maquina.comprar_lata("coca",1000))
print(maquina.comprar_lata("coca",300))
maquina.recarga("coca",-2)
maquina.recarga("sprite",2)
maquina.cambio_precio(400)
maquina.cambio_precio(550)
maquina.estado_maquina()