# import tkinter as tk

# def calcular():
#     num1 = int(entry.get())
#     num2 = int(entry2.get())

#     if operacion.get() == "Suma":
#         resultado = num1 + num2
#     else:
#         resultado = num1 - num2
    
#     label_resultado.config(text="Resultado: " + str(resultado))

# # Crear la ventana principal
# ventana = tk.Tk()
# ventana.geometry("500x400")
# ventana.title("Calculadora")

# # Crear los widgets
# label1 = tk.Label(ventana, text="Número 1:")
# label1.pack()

# entry = tk.Entry(ventana)
# entry.pack()

# label2 = tk.Label(ventana, text="Número 2:")
# label2.pack()

# entry2 = tk.Entry(ventana)
# entry2.pack()

# operacion = tk.StringVar()
# operacion.set("Suma")

# radio_suma = tk.Radiobutton(ventana, text="Suma", variable=operacion, value="Suma")
# radio_suma.pack()

# radio_resta = tk.Radiobutton(ventana, text="Resta", variable=operacion, value="Resta")
# radio_resta.pack()

# one_calcular = tk.Button(ventana, text="Calcular", command=calcular)
# one_calcular.grid(row=0,column=1)

# label_resultado = tk.Label(ventana, text="Resultado:")
# label_resultado.pack()

# # Ejecutar la ventana
# ventana.mainloop()

import tkinter as tk

def sumar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 + num2)

def restar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 - num2)

def multiplicar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 * num2)

def dividir():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    if num2 == 0:
        resultado_var.set("No se puede dividir por cero")
    else:
        resultado_var.set(num1 / num2)

def limpiar():
    numero1_entry.delete(0, tk.END)
    numero2_entry.delete(0, tk.END)
    resultado_var.set("")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x400")

numero1_label = tk.Label(ventana, text="Primer número:")
numero1_label.pack(pady=10)

numero1_entry = tk.Entry(ventana)
numero1_entry.pack()

numero2_label = tk.Label(ventana, text="Segundo número:")
numero2_label.pack(pady=10)

numero2_entry = tk.Entry(ventana)
numero2_entry.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.grid(row=0,column=0)
boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.grid(row=0,column=1)
boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.grid(row=0,column=3)
boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.grid(row=0,column=4)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=0,column=5)

resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var)
resultado_label.pack(pady=10)

ventana.mainloop()