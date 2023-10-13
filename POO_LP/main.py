# en nombre siempre deberia ser en singular y con la primera letra mayuscula
class Perro:
    nombre="boby"
    edad="2 meses"
    color="cheqche"
    raza="chusterrier"

    def ladrar(self):
        return "gua gua mascota"
    def correr(self):
        return ".. .. .. .. .."
    def saltar(self):
        return "brinca alto"
    
    

respuesta=Perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.correr())
print(respuesta.saltar())