class Electrodomestico:
    COLOR_DEF = "blanco"
    CONSUMO_ENERGETICO_DEF = 'F'
    PRECIO_BASE_DEF = 100
    PESO_DEF = 5

    def __init__(self, precio_base=PRECIO_BASE_DEF, peso=PESO_DEF, consumo_energetico=CONSUMO_ENERGETICO_DEF,
                 color=COLOR_DEF):
        self.precio_base = precio_base
        self.peso = peso
        self.consumo_energetico = self.comprobar_consumo_energetico(consumo_energetico)
        self.color = self.comprobar_color(color)

    def comprobar_consumo_energetico(self, consumo_energetico):
        return consumo_energetico if 'A' <= consumo_energetico <= 'F' else self.CONSUMO_ENERGETICO_DEF

    def comprobar_color(self, color):
        colores = ["blanco", "negro", "rojo", "azul", "gris"]
        return color if color in colores else self.COLOR_DEF

    def precio_final(self):
        plus = 0
        if self.consumo_energetico == 'A':
            plus += 100
        elif self.consumo_energetico == 'B':
            plus += 80
        elif self.consumo_energetico == 'C':
            plus += 60
        elif self.consumo_energetico == 'D':
            plus += 50
        elif self.consumo_energetico == 'E':
            plus += 30
        elif self.consumo_energetico == 'F':
            plus += 10

        if 0 <= self.peso < 19:
            plus += 10
        elif 20 <= self.peso < 49:
            plus += 50
        elif 50 <= self.peso <= 79:
            plus += 80
        elif self.peso >= 80:
            plus += 100

        return self.precio_base + plus

class Lavadora(Electrodomestico):
    CARGA_DEF = 5

    def __init__(self, precio_base=Electrodomestico.PRECIO_BASE_DEF, peso=Electrodomestico.PESO_DEF,
                 consumo_energetico=Electrodomestico.CONSUMO_ENERGETICO_DEF,
                 color=Electrodomestico.COLOR_DEF, carga=CARGA_DEF):
        super().__init__(precio_base, peso, consumo_energetico, color)
        self.carga = carga

    def precio_final(self):
        plus = super().precio_final()
        if self.carga > 30:
            plus += 50
        return plus

class Television(Electrodomestico):
    RESOLUCION_DEF = 20

    def __init__(self, precio_base=Electrodomestico.PRECIO_BASE_DEF, peso=Electrodomestico.PESO_DEF,
                 consumo_energetico=Electrodomestico.CONSUMO_ENERGETICO_DEF,
                 color=Electrodomestico.COLOR_DEF, resolucion=RESOLUCION_DEF, sintonizador_tdt=False):
        super().__init__(precio_base, peso, consumo_energetico, color)
        self.resolucion = resolucion
        self.sintonizador_tdt = sintonizador_tdt

    def precio_final(self):
        plus = super().precio_final()
        if self.resolucion > 40:
            plus += self.precio_base * 0.3
        if self.sintonizador_tdt:
            plus += 50
        return plus
    
#EJECUTABLE
def main():
    lista_electrodomesticos = [
        Electrodomestico(200, 60, 'C', "Verde"),
        Lavadora(150, 30),
        Television(500, 80, 'E', "negro", 42, False),
        Electrodomestico(),
        Electrodomestico(600, 20, 'D', "gris"),
        Lavadora(300, 40, 'Z', "blanco", 40),
        Television(250, 70),
        Lavadora(400, 100, 'A', "verde", 15),
        Television(200, 60, 'C', "naranja", 30, True),
        Electrodomestico(50, 10)
    ]

    suma_electrodomesticos = 0
    suma_televisiones = 0
    suma_lavadoras = 0

    for electrodomestico in lista_electrodomesticos:
        suma_electrodomesticos += electrodomestico.precio_final()
        if isinstance(electrodomestico, Lavadora):
            suma_lavadoras += electrodomestico.precio_final()
        if isinstance(electrodomestico, Television):
            suma_televisiones += electrodomestico.precio_final()

    print(f"La suma del precio de los electrodomesticos es de {suma_electrodomesticos}")
    print(f"La suma del precio de las lavadoras es de {suma_lavadoras}")
    print(f"La suma del precio de las televisiones es de {suma_televisiones}")


if __name__ == "__main__":
    main()