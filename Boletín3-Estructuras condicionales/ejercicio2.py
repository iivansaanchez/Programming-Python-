'''
Created on Sep 26, 2022

@author: estudiante
'''

#Realizar un programa que solicite dos números por teclado e imprima en
#pantalla si son iguales, el primero mayor que el segundo o el primero más
#pequeño que el segundo.

numero = int(input("Introduce un número: "))
numero1 = int(input("Introduce un número: "))

if numero == numero1:
    print("Los números son iguales.")
elif numero > numero1:
    print("El numero " + str(numero) + " es mayor que " + str(numero1))
else:
    print("El numero " + str(numero) + " es menor que " + str(numero1))