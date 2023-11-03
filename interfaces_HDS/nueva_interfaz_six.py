#importamos nuestra libreria
from tkinter import *
#instanciamos nuestra clase Tk()
ventana=Tk()  #clase para crear una ventana
ventana.title("clase radiobutton")  # haciendo uso del metodo title para el titulo de mi ventana

ventana.geometry("400x300") # haaciendo uso del metodo geometry para asignarle un tamaño de ventana

#instanciar mi clase Label
etiqueta=Label(ventana,text="Radio Buttons") #clase para crear una etiqueta
#indicar la parte de mi ventana que desea mostrar
#puedo usar los metodos grid o pack
etiqueta.config(fg="green",font=12,)
etiqueta.pack()

info=IntVar()

def mostrar_radio():
    # respuesta = "eres masculino" if info.get()==1 else "eres femenino"
    # etiqueta_Respuesta=Label(ventana,text=respuesta)
    # etiqueta_Respuesta.pack()
    if info.get() == 1:
        etiquetaRespuesta=Label(ventana,text="eres masculino")
        etiquetaRespuesta.pack()
    else:
        etiquetaRespuesta=Label(ventana,text="eres femenino")
        etiquetaRespuesta.pack()


radioMasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radioMasculino.pack()
radioFemenino=Radiobutton(ventana,text="Femenino",value=0,variable=info)
radioFemenino.pack()

#instanciar la clase
boton=Button(ventana,text="Enviar",command=mostrar_radio,bg="blue",fg="white")
boton.pack()



#llamar al metodo de Tk que me permitetener persistencia al mostrarlo la ventana
ventana.mainloop()