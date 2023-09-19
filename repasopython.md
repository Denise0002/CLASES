# REPASO PYTHON

## 1.  TIPOS DE DATOS PRIMITIVOS
- **'a':** cadena de texto

- **'hola':** esto tambien es un string

- 'hola soy un string y te saludo'# cadena larga

## OBSERVACION: Todo lo que esta en commilas es un string.
- '100'

- 'false'

- "hola"

# Un string puede estar entre comillas simples o dobles

- **100:**  este es un tipo de dato numerico entero integer
- **2.1:** este es un tipode dato numerico de tipo flotante float
- **False:**  este es un tipo de dato booleano falso
- **True:** tipo de dato booleano verdadero

## Variables
- Es donde almacenamos nuestro tipo de dato
- Esos datos pueden mutar, cambiar o modificar.
- Como creamos una variablepara almacenar nuestros datos.

> **NOTA:** 
Dato es un a imformacion exacta a comparcion de atributo es una informacion exacta
atributo: varia
dato: exacto


1. Darle unnombre significativo o relacionado al dato que estamos 
almacenando.

2. Asignarle algo(indicarle a que dato esta relaciado).-> asignacion (=).

3. Indicar el tipo de dato que se va almacenar -> Darle el dato a guardar.

> Ejemplos:

Primero el dato el dato voy a pedir la edad de Nadine:
```python
edad_nadine=18
```
Segundo dato de nombre de Edwin:
```python
nombre_alumno='edwin'
```
# OPERADORES:
## Operadores Aritmeticos
- Suma **(+)**

- Resta **(-)**

- Multiplicacion **(*)**

- Division **(/)**

### Suma
> suma= 45+12
### Resta
> resta= 45-12
### Multiplicacion
>multi= 2*5
### Division
> divi= 4/2

### **OPERACION=(45+12+23)/4**

**op=15+12+14+13/4**
 
## Operadores de uso Especial

> **suma=45+42** -> Operador suma resultado 87

> **suma='45'+12** -> Operador concatenacion resultado 4512

> **saludo='hola'+'mundo'** -> Concatenacion holamundo

> **saludo2='hola'+' '+'mundo'** -> Concatenar hola mundo

> **saludos='hola'*2** ->holahola

## DATOS ESTRUCTURALES
Son tipos de datos que estan estructurados de alguna manera.

## Lista
Pueden  almacenar distintos tipos de datos en una sola lista.
```python
['nombre',10,Flase]
lista_amigos['jory','edwin','adan','chinita']
```
## Objetos
tambien al igual que las listas almacenan distintos tipos de datos pero con un orden. Para lamacenar datos en un objeto necesitamos especificar un indice y un valor clave  ->valor 
```python
alumno={
    'nombre':'jory',
    'edad':52,
    'sexo':'todos los dias'
}
```
## Conbinar ambas estructuras de datos

```python
alumno={
    'nombre':'jory',
    'edad':30,
    'amigos'['anthony','edwin','china'],
    'direccion':´{
        'departamento':'ayacucho',
        'provincia':'lucanas',
        'distrito':'puquio',
        'jiron':'san peter',
        'numero':152
    }
}
alumnos=[{},{},{}]
```
# FUNCIONES MAS UTILIZADAS DE PYTHON
existen dos tipos
## 1. Propias de lenguaje
que ya vienen creadas e insertadas en python y estan listas para ser usadas
## Estructura de uso de una funcion
tiene el nombre seguido de parentesis podremos pasarle datos que necesita la funcion para ejecutarse
esta es una funcion que nos sirve para mostrar por consola datos
print('hola')

esta funcion nos saber la longitud de una lista o un string
#len nos devuelve un numero 
```python
print(len([1, 5, 6, 7, 8]))
```
Es una funcion que se detiene a esperar que el usuario introdusca informacion
entre parentesis podremos escribr un mensaje que indique que accion realizara el usuario
input('ingresa ingresa')



## MAX
Esta funcion nos muestra el numero mayor de una lista.
```python
Ejemplo:

lista=[45,12,78,3,24,50]
numero_mayor=max(lista)
print(numero_mayor)
```
## MIN
Esta funcion nos muestra el numero menor de una lista.
```python
Ejemplo:

lista=[45,12,78,9,6,12]
numero_menor=min(lista)
print(numero_menor)
```
## Funcion para convertir de un string a un numero entero
```python
Ejemplo:

numero_string='100'
print(type(numero_string))
numero_entero=int(numero_string)

int('100') # ->>   100  ->> entero
```

## Funcion  para convertir un entero a un string
```python
str(100) #  ->>  '100'  ->>  string
```
## APPEND
Funcion de python quenos permite agregar elementos al final de una lista
```python
Ejemplo:

lista=[15,12,78]
elemento=10
lista.append(elemento)
print(lista)
```
## POP
Funcion de pythom que nos permite eliminar los elementos que se encuentran al final de una lista. Pop elimna y almacena lo eliminado(temporalmente).
```python
Ejemplo:

lista=[15,12,78]
eliminado=lista.pop()
print(lista)
print(eliminado)
```
## INSERT
Funcion de python  que nos permite agregar elementos en cualquier posicion de una lista es se le tiene que pasar dos parametro, primero indiacarle el indice y segundo el dato que se va agregar.
```python
Ejemplo:

lista_nombres=['jory','nadine','bichota']
lista_nombre.insert(1,'satan')
print(lista_nombres)
```
## Remove
Funcion de python que nos permite eliminar  elementos de cualquier posicion de una lista, esta funcion recibe solo el elemento que deseamos eliminar.
```python
Ejemplo:

lista=[4,5,6,7,8,]
lista.remove(6)
print(lista)
```
## SPLIT
Funcion que nos permite dividir en una lista una cadena.
```python
Ejemplo:

cadena='Hola como estan'
lista=cadena.split()
print(lista)
url='wwww.google.com/id=70133573
id=url.split('=').pop()
print(id)
```
# Funciones creadas
Funciones  propias 
pasos para crear una funcion popria 
1. Hacer uso de la palabra  reservada def.
2. Definir un nombre de funcion que escriba , que tarea va a realizar.
3. Establecer los parametros que resivira  la funcion entre parentesis().
4. establecer que valor o dato va retornar mi funcion con la palabra reservada return
> OBSERVACION: Tambien podemos  hacer uso  de la funcion print() para retornar un mensaje en nuestra funcion.
Existen dos tipos de funciones los que no revisen ningun parametro y  los que revisen parametros.
```python
def saludo()
print('hola este  es una saludo')
```
- ¿como hacemos uso de la funcion??
- nombre de la funcion o parentesis

## Funcion con para metros
```python
def mi_print(texto):
    print(texto)

    print('hola este es un print de python')
    mi_print('este es mi print creado')

def suma(a+b):
    total=a+b
    return total

mi_print(suma(45,12))   ->>> 57

Ejemplo:

lista=[12,4,45,3,78,1]
mi-print(max(lista)) ---->> 78


def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
     return numero_mayor
mi_print(mi_max(lista))
```
