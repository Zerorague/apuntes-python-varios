
def decorar_print(print_f):
    def funcion_interna(a):
        print("xnxx.com")
        print_f(a)
    return funcion_interna


@decorar_print
def pprint(a):
    print(a)


pprint("hola")
