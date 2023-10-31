from bd import*
class Usuarios:
    def __init__(self, bd_usuarios):
        self.bd_usuarios = bd_usuarios
    
    def actualizar_edad(self, usuario, nueva_edad):
        for user in self.bd_usuarios:
            if user["usuario"] == usuario:
                user["edad"] = nueva_edad
                return True
        return False
    
    def verificar_usuario(self, usuario):
        for user in self.bd_usuarios:
            if user["usuario"] == usuario:
                return True
        return False
    
    def validar_credenciales(self, usuario, password):
        for user in self.bd_usuarios:
            if user["usuario"] == usuario and user["password"] == password:
                return True
        return False

usuarios = Usuarios(bd_usuarios)

# Mostrar todos los datos de los usuarios
for user in usuarios.bd_usuarios:
    print("Usuario:", user["usuario"])
    print("Edad:", user["edad"])
    print("Contraseña:", user["password"])
    print("-------------------")

# Actualizar edad del usuario
if usuarios.actualizar_edad("rata", 17):
    print("Edad actualizada exitosamente.")
else:
    print("El usuario no se encontró en los registros.")

# Verificar si un usuario está registrado
if usuarios.verificar_usuario("mosca"):
    print("El usuario está registrado.")
else:
    print("El usuario no está registrado.")

# Validar credenciales de usuario y contraseña
if usuarios.validar_credenciales("chapulin", "12345"):
    print("Credenciales válidas.")
else:
    print("Credenciales inválidas.")