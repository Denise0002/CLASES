from tkinter import *
from math import sqrt

def click(numero):
    entrada.insert(END, numero)

def borrar():
    entrada.delete(0, END)

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, END)
        entrada.insert(0, "Error")

ventana = Tk()
ventana.title("Calculadora")

entrada =Entry(ventana, font=('Arial', 20))
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in botones:
    Button(ventana, text=button, padx=20, pady=20, font=('Arial', 20), command=lambda b=button: click(b) if b != '=' else calcular()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

Button(ventana, text='√', padx=20, pady=20, font=('Arial', 20), command=lambda: entrada.insert(END, str(sqrt(float(entrada.get())))).grid(row=5, column=0))

ventana.mainloop()
