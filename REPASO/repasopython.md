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
## CONTROLES DE FLUJO

## Decissiones
solo se ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condicision sea verdadera, podemos hacer que si la concision es falsa se ejecute otro codigo.
## Sintaxis
Primero especificar el codigo que se ejecutara si cumple una condicion .
```python
if <condicision>:
el codigo que deseamos ejecutarsi la condicion es verdad
print('esto siempre ejecuta')
```
Si queremos que se ejecute un codigo en caso sea falso 
```python
if <condicion falsa>:
    print('solo imprime si es verdad')
else:
    ('solo imprime si es falso')
Ejemplo 01:

if 15>18:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
Ejmplo 02:

if 15*2===30:
    print('si es verdad  imprime esto')
else:
    print('si es falso imprime esto')
Ejemplo 03:

condicion=True 
if condicion:
    print('si es veradad imprime esto')
else:
    print('si es falso imprime esto')
```
## Ciclos
Existen dos tipos:
## Cuando sabes la cantidad de veces  que vamos a repetir
Para este caso existe el for
sintaxis despues de la palabra reservada for deberemos crear una variable  que almacene el numero que iremos iterar.
```python
Ejemplo 01:

numeros=[45,72,78,1,2]
for i in range:
    print(i)
    
Ejemplo 02:

vocales=[a,e,i,o,u]
for i in vocales:
    print(i)
```
## Cuando no sabemos la cantidad de veces a repetir