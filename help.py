# for n in range(1,6):
#     nombre=input('ingrese un nombre:')
#     print(f'ingresaste {n} veces el nombre')

numero_ganador=50
condicion=True
while condicion:
    numero_ingresado=int(input('ingrese un numero: '))
    if numero_ingresado == numero_ganador:
        print('Ganaste')
        condicion=False
    else:
        print('Sigue intentando')

#     numero_premiado = 1234
# numero_ingresado = int(input("Ingrese un número: "))

# while numero_ingresado != numero_premiado:
#     print("Número incorrecto. Inténtelo nuevamente.")
#     numero_ingresado = int(input("Ingrese otro número: "))

# print("¡Felicidades! Ha ingresado el número premiado. El programa ha finalizado.")