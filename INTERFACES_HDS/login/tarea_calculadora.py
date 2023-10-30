import tkinter as tk

def calcular():
    num1 = int(entry.get())
    num2 = int(entry2.get())

    if operacion.get() == "Suma":
        resultado = num1 + num2
    else:
        resultado = num1 - num2
    
    label_resultado.config(text="Resultado: " + str(resultado))

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("500x400")
ventana.title("Calculadora")

# Crear los widgets
label1 = tk.Label(ventana, text="Número 1:")
label1.pack()

entry = tk.Entry(ventana)
entry.pack()

label2 = tk.Label(ventana, text="Número 2:")
label2.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

operacion = tk.StringVar()
operacion.set("Suma")

radio_suma = tk.Radiobutton(ventana, text="Suma", variable=operacion, value="Suma")
radio_suma.pack()

radio_resta = tk.Radiobutton(ventana, text="Resta", variable=operacion, value="Resta")
radio_resta.pack()

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.grid(row=0,column=1)

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Ejecutar la ventana
ventana.mainloop()