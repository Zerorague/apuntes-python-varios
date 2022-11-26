class areas:
    """esta calse calcula las areas de diferenctes figuras geometricas"""

    def decorador_a2(funcion):
        def funcion_interior(lado):
            """Calcula el area de un cuadrado elevando all cuadrado el lado pasado por parametros ademas se decora la funcion para agregar informacion del proceso"""
            print(f"el area del cuadrado es {round(funcion(lado),3)} m2")
        return funcion_interior

    @decorador_a2
    def area_cuadrado(lado): return pow(lado, 2)

    def areaTriangulo(base, altura):
        """calcula el area de un triangulo tomando la altura y la base por parametros y dividiendo por 2"""
        return "El area del triangulo es {}".format(((base*altura)/2))


# imprime la documentacion asociada a la funcion o lo que sea
# print(areas.area_cuadrado.__doc__)
# help(areas.area_cuadrado)
# help(areas.areaTriangulo)  # sin necesidad de usar el print
help(areas)
