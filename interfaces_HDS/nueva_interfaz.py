#import tkinter -> libreria para la creacion de interfaces grafica
from tkinter import *
#la libreria tkinter tiene grandes clases para la crescion de interfaces
#Tk() -> el mas usado
#Tkk()
#Tcl()
#2. instanciar Tk(como generador de interfaz grafica)
nueva_ventana=Tk()
#3. frame es tambien una clase Frame() para[crear un frame tengo que primero instanciarlo]
menu_principal=Frame()
#4.  montamos o inicializamos el frame
menu_principal.pack()
#5. haciendo uso del metodo del config le damos un tamaño
menu_principal.config(width='200',height='200')
menu_principal.config(bg='blue')
#metodo de Tk( que mantiene la ejecucion del programa en un bucle)
nueva_ventana.mainloop()