
'Primer Ejercicio de Python'

contador3 = 0
contador5 = 0
contador = 0
for i in range(1,101):
    if i % 3  == 0:
        contador3 += 1
        print("fizz")
    if i % 5 == 0:
        print(i)
        contador5 += 1
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        contador += 1

print(contador3)
print(contador5)
print(contador)
