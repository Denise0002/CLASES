# Haciendo uso de la POO crear un objeto para la entidad celular

class Celular:
    nombre="samsung"
    tamaño="15 cm"
    color="rojo"
    marca="claro"

    def encender(self):
        return "bienvenido a claro"
    def llamar(self):
        return "Halo Halo quien es "
    

respuesta=Celular()
print(respuesta.encender())
print(respuesta.llamar())

Haciendo uso de la POO crear un objeto para la entidad vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} de color {self.color} está acelerando.")

#Crear una instancia de Vehiculo
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

# # Utilizar el objeto avion
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
#haciendo uso de la POO crear un objeto para una pc
class PC:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def encender(self):
        print("Encendiendo la PC...")
    
    def apagar(self):
        print("Apagando la PC...")


#Luego puedes crear una instancia de la clase `PC` y llamar a sus métodos:
mi_pc = PC("Lenovo", "Ideapad")
mi_pc.encender()
mi_pc.apagar()

#haciendo uso de la POO crear un objeto para una impresora
class Impresora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def imprimir(self, documento):
        print(f"Imprimiendo '{documento}' en la impresora {self.marca} {self.modelo}")


# Ejemplo de uso:
mi_impresora = Impresora("Epson", "L210")
mi_impresora.imprimir("MiDocumento.pdf")

#haciendo uso de la POO crear un objeto para una factura
class Factura:
    def __init__(self, numero, cliente, total):
        self.numero = numero
        self.cliente = cliente
        self.total = total

    def imprimir_factura(self):
        print("Factura número:", self.numero)
        print("Cliente:", self.cliente)
        print("Total:", self.total)

#Crear una instancia de la clase Factura
factura1 = Factura(001, "Cliente A", 100.50)
#Llamar al método imprimir_factura para mostrar los detalles de la factura
factura1.imprimir_factura()
