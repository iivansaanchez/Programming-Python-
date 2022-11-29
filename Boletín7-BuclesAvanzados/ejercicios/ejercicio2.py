'''
Created on 24 oct 2022

@author: ivansanchezsanchez

Diseñar un programa que pida dos números enteros y nos muestre 
los siguientes números que son múltiplos del segundo introducido a partir 
del primero. Por ejemplo, si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77 
(a partir de 13 los siguientes 10 múltiplos de 7)
'''
num1 = int(input("Introduce un numero: "))
while num1 <= 0:
    num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
while num2 <= 0:
    num2 = int(input("Introduce otro numero: "))
print(f"{num1} y {num2}")

contador = 10
contadorMultiplo = num2
while contador > 0:
    if contadorMultiplo > num1:
        print(contadorMultiplo)
        contadorMultiplo =  contadorMultiplo + num2
        contador-=1
    else:
        contadorMultiplo =  contadorMultiplo + num2
