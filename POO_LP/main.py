# en nombre siempre deberia ser en singular y con la primera letra mayuscula
class Perro:
    nombre="boby"
    edad="2 meses"
    color="cheqche"
    raza="chusterrier"

    def ladrar(self):
        return "gua gua mascota"
    def corre(self):
        return ".. .. .. .. .."
    

respuesta=Perro()
print(respuesta.nombre)
print(respuesta.ladrar())