# Crear un programa que me pida la edad de uan persona si la edad 
# es mayor o igual a 18  que me muestre un mensaje 'eres mayor de edad'
# caso contrario  que me muestre una mensaje 'ers menor de edad'

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')


monto_compra = float(input("Ingrese el moto de la compra"))
if monto_compra >= 1000:
    descuento = monto_compra *0.2
    monto_final = monto_compra-descuento