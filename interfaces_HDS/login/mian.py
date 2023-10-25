#mporta base de datos
from bd import *
def bd_usuarios(self,bd_usuarios,nombre_usuario):
        respuesta=list(filter(lambda el:el
        ["usuario"]==nombre_usuario,
        bd_usuarios))
        return respuesta

def edad_usuario(self,bd_usuarios):
        respuesta=list(filter(lambda el:el
        ["edad"]==edad_usuario,
        bd_usuarios))
        return respuesta

def eliminar_password(self,bd_usuarios,password):
        respuesta=list(filter(lambda el:el["password"],
        bd_usuarios))
        return respuesta

def actualizar_dni(self,bd_,dni):
        respuesta=list(filter(lambda el:el["dni"],
        bd_usuarios))
        return respuesta
    
nombre=usuarios()
# print(gerente.tienda_gerente(negocios,"china"))
# print(gerente.tienda_mas_categorias(negocios))
# print(gerente.ruc_nombre(negocios))
print(usuarios.edad_usuario(usuarios,18))
print(usuarios.eliminar_password(usuarios,1234))
print(usuaro.actulizar_dni(usuarios,"123456"))