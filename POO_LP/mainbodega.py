from bd import *
class Tiendas_comerciales:

    def bd_gerente(self,bd_negocios,
        nombre_gerente):
        respuesta=list(filter(lambda el:el
        ["gerente"]==nombre_gerente,
        bd_negocios))
        return respuesta
    
    def tienda_mas_categorias(self,bd_negocios):
        respuesta=list(filter(lambda el:len(el
        ["categoria"])>2,bd_negocios))
        return respuesta

    def ruc_nombre(self,bd_negocios):
        respuesta=list(map(lambda el:{
            "nombre_negocio":el["nombre"],
            "ruc_negocio":el["ruc"]
        },bd_negocios))
        return respuesta

    def eliminar_negocio(self,bd_negocios,ruc):
        respuesta=list(filter(lambda el:el["ruc"]
        !=ruc,bd_negocios))
        return respuesta

    def actualizar_negocio(self,bd_negocios,horario_atencion):
        respuesta=list(filter(lambda el:el
        ["hora"]==horario_atencion,
        bd_negocios))
        return respuesta
        
    #otro metodo para crear un nuevo producto





    #otro metodo para actualizar el horario de atencion


    def mostrar_todo(self):
        pass
    
gerente=Tiendas_comerciales()
# print(gerente.tienda_gerente(negocios,"china"))
# print(gerente.tienda_mas_categorias(negocios))
# print(gerente.ruc_nombre(negocios))
print(gerente.eliminar_negocio(negocios,1234))
print(gerente.eliminar_negocio(negocios,123456789))
print(gerente.actulizar_negocio(negocios,"chinaa"))