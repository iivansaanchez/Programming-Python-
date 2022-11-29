'''
Created on 24 oct 2022

@author: ivansanchezsanchez
Diseñar un programa que muestre, para cada número introducido
 por teclado, si es par, si es positivo y su cuadrado. 
 El proceso se repetirá hasta que el número introducido por 
 teclado sea 0. Por ejemplo:
 
    4 ⇒ es par, positivo y su cuadrado es 16
    7 ⇒ es impar, negativo y su cuadrado es 49
'''
num1 = int(input("Introduce un número: "))
while num1 == 0:
    num1 = int(input("El número no es válido. Introduce un número: "))
while num1 != 0:
    cuadrado = 2
    cuadrado = num1 ** cuadrado
    if num1 >= 0:
        if num1 % 2 == 0:
            print(f"{num1} ⇒ Es par, positivo y su cuadrado es {cuadrado}")    
        elif  num1 % 2 != 0:
            print(f"{num1} ⇒ Es impar, positivo y su cuadrado es {cuadrado}")
    else:
        if num1 % 2 == 0:
            print(f"{num1} ⇒ Es par, negativo y su cuadrado es {cuadrado}")
        elif num1 % 2 != 0:
            print(f"{num1} ⇒ Es impar, negativo y su cuadrado es {cuadrado}")
    num1 = int(input("Introduce un número: "))
print(f"El número introducido es {num1}, se acaba el programa")