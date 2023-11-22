# from rich import print   # importacion de la libreria RICH

# class Mascota:
#     def __init__(self):
#         self.nombre=None
#         self.edad=None
#         self.tipo_animal=None
#     def hablar(self,sonido):
#         return sonido
#     def datos_mascota(self,nombre,edad,tipo_animal):
#         self.nombre=nombre
#         self.edad=edad
#         self.tipo_animal=tipo_animal

# #Repaso de programacion orientado a objetos
# class Perro(Mascota):
#     def atacar(self):
#         return "ladra y muerde"
# class Gato(Mascota):
#     pass
    
# perro_boby=Perro()
# perro_boby.datos_mascota("boby",14,"perro")
# print(f"[bold green]perro_boby.hablar('guauu guauu')") # rich de la comilla exterior
# print(f"[bold blue]"+perro_boby.atacar())  # rich comilla interior
# print(f"[bold blue]"+perro_boby.nombre+" "+perro_boby.tipo_animal)  # doble mas (+( +" "+))

class Persona:
    def __init__(self,nombre:str,edad:int,sexo:str):
        return Persona
    def comen(self,plato_favorito:str):
        return f"yo {self.nombre} estoy comiendo mi {plato_favorito}"
    def cagan(self):
        return "pip popo"

class estudiante(Persona):
    def __init__(self,nombre:str,edad:int,sexo:str,carrera_profesional:str):
        super().__init__(nombre,edad,sexo)
        self.carrera_profesional=carrera_profesional
    def estudiar(self):
        return "estoy estudiando POO"
class trabajador:
    def __init__(self,nombre:str,edad:int,sexo:str,profesion:str):
        super().__init__(nombre,edad,sexo)
        self.profesion=profesion
    def trabajar(self):
        return "estoy trabajando POO"
    

persona_estudiante=estudiante()
print(estudiante.estudiar('lomo saltado'))