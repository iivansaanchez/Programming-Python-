'''
Created on Oct 17, 2022

@author: estudiante
Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
“Enter one number:”
“The product is XX
'''

numA =int(input("Introduzca un número: "))
numB = int(input("Introduzca otro número: "))

multiplicacion = 0
for i in range (1, numB+1):
    multiplicacion += numA
print(multiplicacion)
