
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


