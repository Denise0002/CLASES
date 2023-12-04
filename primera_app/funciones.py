from tkinter import *
from tkinter.messagebox import *

from LOS USUARIOS.usuarios import usuarios
#creamos nuestra base de datos
db = orm.SQLiteORM("biblioteca.db")
db.crear_tabla(Usuarios)

#funcion limpiar


def f_limpiar(ventana):
   ventana.nombre_texto.delete(0,END)
   ventana.apellidos_texto.delete(0,END)
   ventana.celular_texto.delete(0,END)
   

   ventana.nombre_texto.focus()

def f_nuevo(ventana):
   nombre=ventana.nombre_texto.get()
   apellidos=ventana.apellidos_texto.get()
   celular=ventana.celular_texto.get()
   showinfo(title="Nuevo",message="nuevo contacto agregado")

   ventana.tabla_datos.insert("",END,text=nombre,values=(apellidos,celular))
   f_limpiar(ventana)

def f_eliminar(ventana):
   elem_eliminar=ventana.tabla_datos.selection()
   showinfo(title="Eliminar",message="Registro eliminado")
   print(ventana.tabla_datos.delete(elem_eliminar))

def f_actualizar(ventana):
   if ventana.nombre_texto.get()=="":
      showerror(title="Sin datos",message="No hay nada que registrar")
   else:
      nombre=ventana.nombre_texto.get()
      apellidos=ventana.apellidos_texto.get()
      celular=ventana.celular_texto.get()
      elem_actualizar=ventana.tabla_datos.selection()
      mensaje=askyesno(title="Actualizar",message="Deseas actualizar el registro")
      if mensaje == True:
         f_limpiar(ventana)
         ventana.tabla_datos.selection_remove(elem_actualizar)
         return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))
      else:
         showinfo(title="No actualizo",message="No se actualizo ningun registro")
         f_limpiar(ventana)
         ventana.tabla_datos.selection_remove(elem_actualizar)

      
      

def f_dobleClick(ventana,event):
   elem_actualizar=ventana.tabla_datos.selection()
   captura_datos=ventana.tabla_datos.item(elem_actualizar)
   mensaje=askyesnocancel(title="Actualizar",message="Desea actualizar los datos")
   if mensaje == True:
      nombre=captura_datos["text"]
      apellido=captura_datos["values"][0]
      celular=captura_datos["values"][1]
      ventana.nombre_texto.insert(0,nombre)
      ventana.apellidos_texto.insert(0,apellido)
      ventana.celular_texto.insert(0,celular)
      ventana.tabla_datos.selection_remove(elem_actualizar)
   else:
      showinfo(title="Actualizar",message="Ningun registro seleccionado para actualizar")
      ventana.tabla_datos.selection_remove(elem_actualizar)
