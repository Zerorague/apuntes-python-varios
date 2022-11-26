# ----------propiedades---------
class Coche:
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    enmarcha = False

    # ----------Metodos-------------

    def arrancar(self):
        self.enmarcha = True

    def frenar(self):
        self.enmarcha = False

    def estado(self):
        if self.enmarcha:
            print("brrrrrrmmmmm brmmmmm")
        else:
            print("tin tin tin")
        print(f"el numero de ruedas es {self.ruedas}")

    def numero_ruedas(self, ruedas) -> int:
        self.ruedas = ruedas


auto = Coche()

auto.estado()
auto.arrancar()
auto.numero_ruedas(0)
auto.frenar()
auto.estado()

auto2 = Coche()
