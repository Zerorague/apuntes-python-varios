class vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self,arrancar):
        if arrancar:
            self.enmarcha==True
    
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print(f"""Marca: {self.marca}, modelo: {self.modelo}.\nEn marcha: {self.enmarcha}, Acelera: {self.acelera}, Frenado: {self.frena}""")

class moto(vehiculos):    #asi se heradaaaaaaaa   
    pass

mimoto=moto("Honda","CBR")

mimoto.estado()