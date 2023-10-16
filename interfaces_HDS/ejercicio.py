from tkinter import *

ventana=Tk()
#instancio mi primer widget
widget_uno=Frame()

#usar metodo para mostrar el frame }
widget_uno.grid(row='1',column='0')
widget_uno.config(width='100', height='100')
widget_uno.config(bg='blue')

widget_dos=Frame()

#usar metodo para mostrar el frame }
widget_dos.grid(row='1',column='3')
widget_dos.config(width='100', height='100')
widget_dos.config(bg='green')

widget_tres=Frame()

#usar metodo para mostrar el frame }
widget_tres.grid(row='3',column='0')
widget_tres.config(width='100', height='100')
widget_tres.config(bg='red')

widget_cuatro=Frame()

#usar metodo para mostrar el frame }
widget_cuatro.grid(row='3',column='3')
widget_cuatro.config(width='100', height='100')
widget_cuatro.config(bg='red')

ventana.mainloop()

