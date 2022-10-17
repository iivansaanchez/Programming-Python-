'''
Created on Oct 17, 2022

@author: estudiante

Design a program that reads a positive number N greater than 0 and show the result
of the sum of the N numbers between 1 and N. If the number N is not valid, the
program should ask for it again. The messages are the following:
“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX.
'''

num = int(input("Introduce un número mayor que 0: "))
while num <= 0:
    num = int(input("El número introducido no es válido. Introduce un número mayor que 0: "))
sumaNumero = 0   
for i in range (1, num):
    sumaNumero+=i
    print(sumaNumero)
