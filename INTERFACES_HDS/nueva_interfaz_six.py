from tkinter import *

def verificar_datos():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    if usuario == "Yuky" and contraseña == "246801":
        mensaje.config(text="Bienvenido a Facebook")
    else:
        mensaje.config(text="Ingrese bien sus datos",fg="red")

# Crear la ventana principal
ventana = Tk()
ventana.geometry("300x350")
ventana.title("Facebook")
# ventana.title("Formulario de Inicio de Sesión")

# Crear etiquetas y entradas
etiqueta_usuario = Label(ventana, text="Usuario:")
etiqueta_usuario.config(bg="white",fg="blue")
etiqueta_contraseña = Label(ventana, text="Contraseña:")
etiqueta_contraseña.config(bg="white",fg="blue")
entrada_usuario = Entry(ventana)
entrada_contraseña = Entry(ventana, show="*")  # Para ocultar la contraseña

# Crear botón de verificación
boton_verificar = Button(ventana, text="Iniciar Secion", command=verificar_datos,bg="green",fg="white")

# Crear etiqueta para mostrar el mensaje
mensaje = Label(ventana, text="")

# Colocar widgets en la ventana
etiqueta_usuario.pack()
entrada_usuario.pack()
etiqueta_contraseña.pack()
entrada_contraseña.pack()
boton_verificar.pack()
mensaje.pack()

# Iniciar la aplicación
ventana.mainloop()