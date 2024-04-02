
print(""" 
      Bienvenido a la calculadora Dinamica
      Las operaciones que puedes realizar son : suma,resta,division, multiplicacion
      Para Salir escribe ("salir")
      """)
bandera = 1
cadena = []
while bandera >0:
    
    if len(cadena) >= 0:
        numero = int(input("Ingresa un numero: "))
        operador = input("Elige la operacion: ")
        
        if operador == "suma":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = numero + numero1
        if operador == "resta":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = numero - numero1
        if operador == "division":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = numero / numero1
        if operador == "multiplicacion":
            numero1 = int(input("Ingresa el siguiente numero: "))
            resultado = numero * numero
        print(f"El resultado es {resultado}")

    cadena.append(resultado)
    if operador == "salir":
        break

