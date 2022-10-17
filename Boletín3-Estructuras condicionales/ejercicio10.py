'''
Created on Sep 29, 2022

@author: estudiante
'''
#Realizar un programa que lea un carácter y dos números enteros por
#teclado. Si el carácter leído es un operador aritmético, calcular la operación
#correspondiente, si es cualquier otro debe mostrar un error.

numero1 = int(input("Introduce el número 1: "))
numero2 = int(input("Introduce el número 2: "))
operador = input("Introduce la operacion +, -, *, /: ")

if operador == "+":
    suma = numero1 + numero2
    print("La suma de los número introducidos es: %s"(suma))
elif operador == "-":
    resta = numero1 - numero2
    print("La resta de los número introducidos es: %s"(resta))
elif operador == "*":
    multiplicacion = numero1 * numero2
    print("La multi`plicacion de los número introducidos es: %s"(multiplicacion))
elif operador == "/":
    division = numero1 / numero2
    print("La division de los número introducidos es: %s"(division))
    
else:
    print("Los valores introducidos no son válidos")
