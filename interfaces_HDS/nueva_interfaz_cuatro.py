from tkinter import *
ventana=Tk()
ventana.title("mi ventana")
ventana.geometry("500x400")

# column_izquierda=Frame()
# column_izquierda.grid(row=0,column=0)
# column_izquierda.config(width=200,height=5)
# etiqueta=Label(ventana,text="esta es mi etiqueta")
# etiqueta.grid(row=0,column=1)
# etiqueta.config(bg='red')

header=Frame()
header.grid(row=0,column=0,columnspan=4)
header.config(width=500,height=15,bg='red')

aside_left=Frame()
aside_left.grid(row=1,column=0,columnspan=7)
aside_left.config(width=15,height=385,bg='red')

etiqueta_usuario=Label(ventana,text="Usuario").grid(row=1,column=1)
text_usuario=Entry(ventana).grid(row=1,column=2)

section_uno=Frame()
section_uno.grid(row=2,column=1,columnspan=2)
section_uno.config(height=2,bg='red')

etiqueta_password=Label(ventana,text="Usuario").grid(row=3,column=1)
text_usuario=Entry(ventana,show=('*')).grid(row=3,column=2)

# txt_passwork=Entry(ventana,show="#")  --> no reemplace el texto real que ingresamos
# text_passwork.get() --> capturar lo que se ingrese en mi cuadro de texto
# text_passwork.delete(0,END) ---> eliminar todo el contenido
# texto_passwork.insert(0. "ingrese nombre") --> insertar texto en el cuadrado

# text.passwork.Focus()

#boton_Enviar=Button(ventana,text="Enviar",command=)
def captura_usurio():
    usuario=text_usuario.get()
    info_usuario=Label(ventana,text=f"{usuario}¡").grid(row=2,column=2)
    text_usuario.delete(0,END)
    return info_usuario

boton_cancelar=Button(ventana,text="cancela",command=limpiar_text)
boton_cancelar.grid(row=2,column=0)

def limpiar_text():
    text_usuario.delete(0,END)
    text_passwork.delete(0,END)
    text_usuario.focus()

ventana.mainloop()