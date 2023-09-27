# Haciendo uso de la POO crear un objeto para la entidad celular

class Celular:
    nombre="samsung"
    tamaño="15 cm"
    color="rojo"
    marca="claro"

    def nombre(self):
        return "bienvenido a claro"
    def color(self):
        return "el de un color"
    

respuesta=Celular()
print(respuesta.nombre)
print(respuesta.color())

# Haciendo uso de la POO crear un objeto para la entidad vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} de color {self.color} está acelerando.")

# Crear una instancia de Vehiculo
vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

# Utilizar el objeto vehiculo
vehiculo.acelerar()




# Haciendo uso de la POO crear un objeto para la entidad avion
class Avion:
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def despegar(self):
        print(f"El avión {self.marca} {self.modelo} con capacidad de {self.capacidad} despegó.")

# Crear una instancia de Avion
avion = Avion("Boeing", "747", 300)

# Utilizar el objeto avion
avion.despegar()

# Haciendo uso de la POO crear un objeto para la entidad dota2
class HeroeDota:
    def __init__(self, nombre, tipo, habilidad_principal):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidad_principal = habilidad_principal

    def usar_habilidad(self):
        print(f"El héroe {self.nombre} está usando su habilidad principal: {self.habilidad_principal}.")

# Crear una instancia de HeroeDota
heroe = HeroeDota("Invoker", "Inteligencia", "Sun Strike")

# Utilizar el objeto heroe
heroe.usar_habilidad()
