
# Ejecicio 1 
# Programa de indice de masa corporal
# Parametros 

""""
from cmath import sqrt


peso = int(input("Peso: "))
estatura = float(input("Estatura: "))

def calculaIMC(peso, estatura):
    IMC = peso/ (estatura**2)
    return IMC

def EvaluaIMC(IMC):
        if IMC <16:
              print("Delgadez severa")
        if  IMC >= 16 and IMC < 17:
              print("Delgadez moderada")
        if  IMC >= 17 and IMC < 18.5:
              print("Delgadez leve")
        if IMC >=17 and IMC < 18.9:
              print("Delgadez leve")
        if IMC >= 18.5 and IMC < 25: 
              print("Peso Normal")
    
        return IMC

# Ejecucucion del programa 

IMC = calculaIMC(peso, estatura)
IMC = EvaluaIMC(IMC)
print("El IMC es: ", IMC)
# Programa de indice de masa corporal


################################################################
################## EJERCICO 2 ##################################
################################################################

# Las raices de una ecuacion cuadratica 


def ParametrosEcuacion(a,b,C):
    x_1 = complex((b + sqrt(b**2 - (4*a*C)))/(2*a))
    x_2 = complex((-b - sqrt(b**2 - (4*a*C)))/(2*a))
    return f"Las solucion de la ecuaciones {x_1} y {x_2}"

# Ejecucion del programa 
Ecuacion =  ParametrosEcuacion(3,2,1)
print(Ecuacion)

################################################################
# Año bisiesto
def AñoBisiesto(Año):
    if Año % 4 == 0 and Año % 100!= 0 or Año % 400 == 0:
        return f"El año {Año} es bisiesto"
    else:
        return f"El año {Año} es no bisiesto"
    
año = AñoBisiesto(2016)
print(año)

"""
"""""
## Numero de Amstrong 
def NumeroAmstrong(numero):
    numeroStr = str(numero)
    sumaTotal = 0
    for i in numeroStr:
        numero1 = int(i)
        suma = numero1**len(numeroStr)
        sumaTotal = sumaTotal + suma
    return sumaTotal

NumeroAmstrong1 = NumeroAmstrong(371)
print(NumeroAmstrong1)

## Ejercio de la suma armonica asta el enecimo numero 
def sumaArmonica(numero):
    variable = 1
    divide = 1/variable
    suma = 0
    while variable <= numero:
        divide = 1/variable 
        variable = variable + 1
        suma = suma + divide
    return suma

## Funcion armocica de la suma con for

def SumaArmonica(numero):
    suma = 0
    num = 1
    for num in range(num, numero +1):
        suma = suma + 1/num
    return suma

#Ejecucucion 

numero = int(input("Ingrese numero: "))
suma = sumaArmonica(numero)
numero1 = int(input("Ingrese numero: "))
suma1 = SumaArmonica(numero1)
print(suma)
print(suma1)

"""

# Conteo de cuantos dijitos tiene un numero

""""
def NumeroDijitos(numero):

    numeroStr = str(numero)
    contador = 0
    for caracter in numeroStr:
        contador += 1
    return contador

numero = int(input("Ingrese numero: "))
numeroDijitos = NumeroDijitos(numero)
print(numeroDijitos)
   
"""
# Numeros de divisores de un numero
def NumerosDivisores(numero):
    contador = 1
    divisores = []
    while contador <= numero:
        if numero%contador == 0:
            divisores.append(contador)
        contador += 1
    return divisores

""""
numero = int(input("Ingrese numero: "))
numeroDivisores = NumerosDivisores(numero)
print(numeroDivisores)
"""
# Numeros amigos
def NumerosAmigos(numero1, numero2):
    divisores1 = NumerosDivisores(numero1)
    divisores2 = NumerosDivisores(numero2)
    suma = 0;suma1 = 0
    for i in divisores1:
        suma = suma + i
    for j in divisores2:
        suma1 = suma1 + j
    if suma == suma1:
        return "Numeros amigos"
    else:
        return "Numeros no amigos"

""""
numero1 = int(input("Ingrese numero1: "))
numero2 = int(input("Ingrese numero2: "))
numeroAmigos = NumerosAmigos(numero1, numero2)
print(numeroAmigos)

"""
##  Factorial de un numero
""""
def factorial(numero):
    contador  =1
    factorial = 1
    while contador <= numero:
        factorial = factorial * contador
        contador += 1
    return factorial

numero = int(input("Ingrese numero: "))
factorial = factorial(numero)
print(factorial)
"""
## Maximo comun divisor de un numero ### 

def MCD(numero1, numero2):
    variable_divisor = NumerosDivisores(numero1)
    variable_divisor1 = NumerosDivisores(numero2)
    respuesta = 1
    contenedor = []
    for i in variable_divisor:
        for j in variable_divisor1:
            if i == j:
                contenedor.append(i)
    else:
        respuesta = max(contenedor)
    return respuesta

## MCM ### 

def MCM(numeros1, numeros2):
    solucion = (numeros1*numeros2)/MCD(numeros1,numeros2)
    return solucion

## Ejecucion del programa ## 
""""
numeros1 = int(input("Ingresa el primer numero divisor: "))
numeros2 = int(input("Ingresa el primer numero divisor: "))
print(MCM(numeros1, numeros2))

numeros1 = int(input("Ingresa el primer numero divisor: "))
numeros2 = int(input("Ingresa el primer numero divisor: "))

print(MCD(numeros1, numeros2))            

"""
#### Elementos Duplicados en un array #####

""""
def CreaArray(numero_elementos):
    elemento = []
    while numero_elementos > len(elemento):
        elemento_pedido = int(input("Ingresa el elemento: "))
        elemento.append(elemento_pedido)
    
    bandera = 1
    elementos_repetidos = []
    for element in elemento:
        if bandera == len(elemento):
            break
        if element == elemento[bandera]:
            elementos_repetidos.append(element)
        bandera = bandera +1
    im_elementos = ""
    for i in elementos_repetidos:
        im_elementos = im_elementos + " "+ str(i)

## Busqueda de un elemento #####
    elemento_busqueda = int(input("Elemento a buscar: "))
    for i in elemento:
        if i == elemento_busqueda:
            print(f"Elemento encontrado {elemento_busqueda}")
            break

    return f"Los elementos repetidos son: {im_elementos}"
#array = CreaArray(5)
#print(array)

## Ejercicios de programacion Lunes ####
## Ejercicio 1 ####
## Busqueda de elementos comunes en dos arrays ####
"""

## Funcion que cre listas ### 

def CreaArray():
    numero_elementos = int(input("Numero de elementos de array: "))
    array = []
    while numero_elementos > len(array):
        elmento = input("Ingresa elemento: ")
        array.append(elmento)
    return array
def elementos_comunes(array1, array2):
    array_elementos_comunes = []
    for i in array1:
        for j in array2:
            if i == j:
                array_elementos_comunes.append(i)
    return array_elementos_comunes

## Ejecucion ## 
arra1 = CreaArray() ; arra2 = CreaArray()
ejecucion = elementos_comunes(arra1,arra2)
print(ejecucion)

# TERMINO DE LO EJERCICIOS BASICOS PARA APRENDER LOS CONSEPTOS DEL LENGUAJE DE PROGRMACION PYTHON ## 

print("Mwensaje de Finalizacuion")

#Mensaje de Finalizacuion    









