class Vehiculos():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nAcelera: {self.acelera}\nFrena: {self.frena}")


class Moto(Vehiculos):
    def __init__(self, marca, modelo, valor) -> None:
        super().__init__(marca, modelo)
        self.caballito = False
        self.valor = valor

    def estado(self):
        super().estado()
        print(f"caballito: {self.caballito}\nvalor: ${self.valor}")


miMoto = Moto("Honda", "CBR", 900000)
miMoto.estado()

print("--------------cambio--------------")

miAuto = Vehiculos("Nissan", "V16")
miAuto.estado()
