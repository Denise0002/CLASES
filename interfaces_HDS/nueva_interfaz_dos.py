#importamos Tkinter
from tkinter import *
#instanciar la clase Tk()
ventana=Tk()
#instancio mi primer widget
widget_uno=Frame()

#usar metodo para mostrar el frame }
widget_uno.grid(row='0',column='0')
widget_uno.config(width='100', height='100')
widget_uno.config(bg='yellow')
#el metodo grid recibe dos parametros el numero de la columnay el numero de fila donde quiero ubicar mi widget

#creacion de un segundo widget
widget_dos=Frame()

widget_dos.grid(row='2',column='0')
widget_dos.config(width='100',height='100')
widget_dos.config(bg='purple')
#creando un tercero widget
widget_tres=Frame()

widget_tres.grid(row='3',column='0')
widget_tres.config(width='100',height='100')
widget_tres.config(bg='red')
# usar el metodo loop para que la ventana mermanesca abierta
ventana.mainloop()

