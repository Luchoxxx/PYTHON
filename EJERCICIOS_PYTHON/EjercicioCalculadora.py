
print(""" 
      Bienvenido a la calculadora Dinamica
      Las operaciones que puedes realizar son : suma,resta,division, multiplicacion
      Para Salir escribe ("salir")
      """)
bandera = 1
cadena = []
n = 0
while bandera >0:
    
    if len(cadena) == 0:
        numero = int(input("Ingresa un numero: "))
        cadena.append(numero)
    operador = input("Elige la operacion: ")

    if len(cadena) > 0:
       
        if operador == "suma":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] + numero1
            print(f"El resultado es {resultado}")

        if operador == "resta":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] - numero1
            print(f"El resultado es {resultado}")

        if operador == "division":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] / numero1
            print(f"El resultado es {resultado}")

        if operador == "multiplicacion":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = cadena[n] * numero1
            print(f"El resultado es {resultado}")

        cadena.append(resultado)
        n = n +1
    else:
            print("Entrada invalida")
    
    if  operador == "salir":
        break

