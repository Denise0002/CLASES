# Crea1. r un programa que me pida la edad de uan persona si la edad 
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
    #2.Una tienda comercial desea hacer un descueto del 20%, crear 
#un programa que me determine si el cliente se hace acreedor del
#descueto teniendo encuenta los siguiente, si el cliente realiza 
#una compra de igual o mayor a 1000 soles mostrar un mensaje que
#diga 'ganaste el descuento del 20% ahora pagaras <mostrar el 
#total de la compra menos el descuento en caso la compra no
#supere los 1000 soles entonces mostrar un mensaje que diga 'no
#aplicas al descuento <mostrar el monto de la compra>'


#monto_compra = float(input("Ingrese el monto de la compra en soles: "))

if monto_compra >= 1000:
   descuento = monto_compra * 0.2
   total_con_descuento = monto_compra - descuento
    print("¡Ganaste el descuento del 20%! Ahora pagarás:", total_con_descuento, "soles.")
else:
    print("No aplicas al descuento. El monto de tu compra es:", monto_compra, "soles.")
    
    
    #3 crear un programa que me pida 5 veces un nombre y por cada vez que lo 
    # pida muestre la cantidad de veces que ingreso el nombre
   
    
    for n in range(1,6):
      nombre=input("ingrese su nombre:")
      print(f"ingresaste {n} veces el nombre")
    
    ##4 crear un programa que pida un numero 
    # y lo evalue con el numero premiado si el
    # numero ingresado es el premiado el programa finalizara si el numero ingresado
    # es incorrecto el programa seguira pidiendo el numero premiado

numero_premiado = 1234
numero_ingresado = int(input("Ingrese un número: "))

while numero_ingresado != numero_premiado:
   print("Número incorrecto. Inténtelo nuevamente.")
   numero_ingresado = int(input("Ingrese otro número: "))

print("¡Felicidades! Ha ingresado el número premiado. El programa ha finalizado.")

##5##crear una funcion por cada operador aritmetico y que resiva 2 parametros 
##y retorne el resdultado de la operacion,ojo. crearse un funcion que nos permita 
##imprimir el ressultado.

apython
def suma(a, b):
   resultado = a + b
   return resultado
def imprimir_resultado(resultado):
 print("El resultado es:", resultado)


#2. Función de resta:
python
def resta(a, b):
    resultado = a - b
    return resultado

def imprimir_resultado(resultado):
   print("El resultado es:", resultado)
 
 
 #6 escribir una funcion que resiva como parametros una lista de numeros y retorne una nueva lisat con el cuadro de numero de la lista ingresada
 
ef calcular_cuadrados(lista):
    cuadrados = []
    for num in lista:
        cuadrados.append(num ** 2)
    return cuadrados




#7 escribe una funcion que reciba un numero entero positivo y devuelva su factorial

 def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
     
     # 8 escribir un programa que reciba una cadena de caracteres y devuelva un objeto con cada palabra que contiene y su frecuencia
     python
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print(resultado)
