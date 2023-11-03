# celulares
# class Celular:
#     atributos
#     modelo='samsung'
#     color='rojito'
#     display='7.8"'

#     funcionalides
#     def llamar(self,destino):
#         return f'llamando a {destino}'
    
#     llamandoJory=Celular()
#     objeto celular
#     print(llamandoJory.modelo)
#     print(llamandoJory.llamar('china'))

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Imagen en Tk")
root.geometry("400x300")
# Cargar imagen del disco.
image = tk.PhotoImage(file="imagen.png")
# Insertarla en una etiqueta.
label = ttk.Label(image=image)
label.pack()
root.mainloop()