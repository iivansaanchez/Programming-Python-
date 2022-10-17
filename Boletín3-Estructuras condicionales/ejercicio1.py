'''
Created on Sep 26, 2022

@author: estudiante
'''

#Realizar un programa que lea un número entero por teclado e informe de si
#el número es par o impar (el cero se considera par).

numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print("Es un número par.")
else:
    print("Es un número impar")
    
    