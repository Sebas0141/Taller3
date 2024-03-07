class Persona:
    SEXO_DEF = 'H'
    INFRAPESO = -1
    PESO_IDEAL = 0
    SOBREPESO = 1

    def __init__(self, nombre="", edad=0, sexo=SEXO_DEF, peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.comprobar_sexo()

    def comprobar_sexo(self):
        if self.sexo != 'H' and self.sexo != 'M':
            self.sexo = self.SEXO_DEF

    def calcular_IMC(self):
        peso_actual = self.peso / (self.altura ** 2)
        if 20 <= peso_actual <= 25:
            return self.PESO_IDEAL
        elif peso_actual < 20:
            return self.INFRAPESO
        else:
            return self.SOBREPESO

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def __str__(self):
        sexo_str = "hombre" if self.sexo == 'H' else "mujer"
        return f"Informacion de la persona:\n" \
               f"Nombre: {self.nombre}\n" \
               f"Sexo: {sexo_str}\n" \
               f"Edad: {self.edad} años\n" \
               f"Peso: {self.peso} kg\n" \
               f"Altura: {self.altura} metros\n"


#Datos del Usuario
nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (H/M): ").upper()
peso = float(input("Introduce el peso: "))
altura = float(input("Introduce la altura: "))

#Creación del Objeto
persona = Persona(nombre, edad, sexo, peso, altura)

#Resultados del ejercicio
print(persona)
print("Mensaje de peso:")
if persona.calcular_IMC() == Persona.PESO_IDEAL:
    print("La persona está en su peso ideal")
elif persona.calcular_IMC() == Persona.INFRAPESO:
    print("La persona está por debajo de su peso ideal")
else:
    print("La persona está por encima de su peso ideal")

#Y mayor o menor de edad
if persona.es_mayor_de_edad():
    print("La persona es mayor de edad")
else:
    print("La persona no es mayor de edad")