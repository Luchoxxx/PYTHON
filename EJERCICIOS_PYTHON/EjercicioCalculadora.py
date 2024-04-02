
print(""" 
      Bienvenido a la calculadora Dinamica
      Las operaciones que puedes realizar son : suma,resta,division, multiplicacion
      Para Salir escribe ("salir")
      """)
cadena = [] # 2,0 -> n + 0
n = 0
while True:
    
    if len(cadena) == 0:
        numero = int(input("Ingresa un numero: "))
        cadena.append(numero)
    operador = input("Elige la operacion: ")

    if len(cadena) > 0:
        resultado = 0
        if operador == "suma":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] + numero1
            print(f"El resultado es {resultado}")

        elif operador == "resta":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] - numero1
            print(f"El resultado es {resultado}")

        elif operador == "division":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] / numero1
            print(f"El resultado es {resultado}")

        elif operador == "multiplicacion":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] * numero1
            print(f"El resultado es {resultado}")
        elif  operador == "salir":
            break
        elif resultado == 0:
            cadena.remove(resultado)    
        else:
            print("Entrada invalida")
            if resultado == 0:
                n = n - 1
        cadena.append(resultado)
        n = n +1
 
   

