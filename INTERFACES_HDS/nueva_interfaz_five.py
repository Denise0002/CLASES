from tkinter import *
ventana= Tk()
ventana.geometry("300x350")
ventana.title("ventana suma")

etiqueta=Label(ventana,text=("introduce tu nombre"))
# etiqueta.grid(row=,column=)
etiqueta.pack()

text_nombre=Entry(ventana)
text_nombre.config(bg="blue",fg=("yellow"))+
text_nombre.pack()


ventana.mainloop()