'''
Created on Oct 11, 2022

@author: estudiante

Design a program that asks how many numbers the user wants to introduce. Then,
the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative
number, it is not valid, and the system should ask for another number. The messages
are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The number XX is odd”
“The number XX is even”

'''

cantidadNum = int(input("¿Cuantos números deseas ingresar?: "))

while cantidadNum > 0:
    numero = int(input("Introduce un número mayor que 0: "))
    while numero <= 0:
        numero = int(input("El número introducido no es válido. Introduce un número mayor que 0: "))
    if numero % 2 == 0:
        print("El número %s es par."%(numero))
        cantidadNum -=1
    else:
        print("EL número %s es impar"%(numero))
        cantidadNum -=1