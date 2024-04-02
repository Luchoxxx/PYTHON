
def serie_basilea(n):
    
    suma = 0
    variable = 0
    while variable < n :
        suma = suma + 1/((variable +1)**2)
        variable = variable + 1

    return suma
#aplicacion 
suma1 = serie_basilea(3)
print(suma1)

# Mensaje de comprobacion 
print("Este programa ejecuta la serie matematica de basilea")
print("Este programa")
#aplicacion

# Agregando un print 
print("Este programa fuer creado por Luis")
