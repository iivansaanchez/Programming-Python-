'''
Created on Oct 17, 2022

@author: estudiante
Design a program that asks for numbers until the user inputs a negative one. When
this happens, the program will show how many positive numbers have been
introduced by the user. The messages are the following:
“Enter a number (negative to finish):”
“You have entered XX positive numbers.”
'''

num = int(input("Introduce un número mayor a 0: "))

contador = 0

while num >= 0:
    num = int(input("Introduce un número mayor a 0: "))
    contador+=1

print("Has introducido %s números positivos"%(contador))
    
