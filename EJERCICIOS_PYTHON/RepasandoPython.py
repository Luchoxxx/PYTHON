## Tipo de variable set ## 
'''
my_set = {}
my_set ={"Luis","Alberto",22}
print(type(my_set))

new_set = set()
new_set.add("Direccion")
print(type(new_set))
print(new_set)
print(len(my_set))
'''

# Ejecicios de repaso para aprender cosas mas Avanzadas en Python 

'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
'''
import time
'''
def son_anogramas(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False
    else:
        return sorted(palabra1) == sorted(palabra2) and palabra1 != palabra2

print(son_anogramas("roma", "amor"))


FIBONACII

def fibonacci(n):
    if n<= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


Es un numero Primo  


def es_primo(n):
    contador = 0
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True
print(es_primo(7))
 '''
'''
    CREAR UNA UNICA FUNCION QUE CACULE EL AREA DE LOS POLIGONOS.

'''
'''
def area_poligono(poligono):
    """
    Calcula el área de un polígono (triángulo, cuadrado o rectángulo).
    El parámetro 'poligono' debe ser un diccionario con la clave 'tipo' y los datos necesarios:
    - Triángulo: {'tipo': 'triangulo', 'base': valor, 'altura': valor}
    - Cuadrado: {'tipo': 'cuadrado', 'lado': valor}
    - Rectángulo: {'tipo': 'rectangulo', 'base': valor, 'altura': valor}
    """
    tipo = poligono.get('tipo', '').lower()
    if tipo == 'triangulo':
        return (poligono['base'] * poligono['altura']) / 2
    elif tipo == 'cuadrado':
        return poligono['lado'] ** 2
    elif tipo == 'rectangulo':
        return poligono['base'] * poligono['altura']
    else:
        raise ValueError("Tipo de polígono no soportado")

# Ejemplos de uso:
triangulo = {'tipo': 'triangulo', 'base': 5, 'altura': 3}
cuadrado = {'tipo': 'cuadrado', 'lado': 4}
rectangulo = {'tipo': 'rectangulo', 'base': 6, 'altura': 2}

print("Área del triángulo:", area_poligono(triangulo))
print("Área del cuadrado:", area_poligono(cuadrado))
print("Área del rectángulo:", area_poligono(rectangulo))

'''
'''
import requests
from PIL import Image
from io import BytesIO
url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
respuesta = requests.get(url)
imagen = Image.open(BytesIO(respuesta.content))
ancho , alto = imagen.size
aspect_ratio = ancho / alto
print("Aspect ratio:", aspect_ratio)
'''
'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''
'''
def invertir_cadena(cadena):

    cadena1 = ""
    for i in range(len(cadena) -1 , -1, -1):
        devuelto = cadena[i]
        cadena1 = cadena1 + devuelto
    return cadena1
print(invertir_cadena("hola"))
'''

'''
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
'''
'''
def contar_palabras(texto):
    texto = texto.lower()
    palabras = {}
    palabra_actual = ""
    
    for char in texto:
        if char.isalnum():  # Verifica si el carácter es alfanumérico
            palabra_actual += char
        else:
            if palabra_actual:
                if palabra_actual in palabras:
                    palabras[palabra_actual] += 1
                else:
                    palabras[palabra_actual] = 1
                palabra_actual = ""
    
    # Para la última palabra si el texto no termina con un espacio o puntuación
    if palabra_actual:
        if palabra_actual in palabras:
            palabras[palabra_actual] += 1
        else:
            palabras[palabra_actual] = 1
    
    return palabras

print(contar_palabras("Hola, hola! ¿Cómo estás? Hola."))
'''
'''
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

'''
def decimal_binario(numero):
    import time
    incio = time.time()
    if numero == 0: 
        return "0"
    else:
        binario = ""
        while numero > 0:
            residuo = numero % 2
            binario = str(residuo) + binario
            numero = numero // 2
    final = time.time()
    print(f"Tiempo de ejecución: {final - incio:.16f} segundos")
    return binario
print(decimal_binario(46474752952895825725725729572525275234723742472472))  # Imprime '1010'