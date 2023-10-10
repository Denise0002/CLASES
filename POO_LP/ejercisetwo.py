#crear un objeto clase laptop con dos atributos de clase y 5 atributos de instancia,  devera tener hasta 3 funcionalidades
#como minimo .
class Laptop:
    marca = ""
    color = ""

    def __init__(self, modelo, precio, memoria_ram, almacenamiento, procesador):
        self.modelo = modelo
        self.precio = precio
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.procesador = procesador

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Memoria RAM: {self.memoria_ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Procesador: {self.procesador}")

    def encender(self):
        print("La laptop está encendiendo...")

    def apagar(self):
        print("La laptop se está apagando...")


# Crear una instancia de la clase Laptop
mi_laptop = Laptop("Levono", 1500, "8GB", "1TB", "Intel Core i7")

# Acceder a los atributos de instancia y llamar a las funcionalidades
mi_laptop.mostrar_informacion()
mi_laptop.encender()
mi_laptop.apagar()
