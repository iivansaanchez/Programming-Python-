'''
Created on 17 oct 2022

@author: ivansanchezsanchez

Design a program that reads an integer positive number and says the “factorial” of 
the number. To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following: “Enter an integer positive number:” 
“The number is not valid, try again.” “The factorial is XX
'''

num = int(input("Introduce un número entero positivo: "))

while num <= 0:
    num = int(input("El número introducido no es válido. Introduce un número entero positivo: "))

valorFact = 0
for i in range(num, 0, -1):
    valorFact+=i

print(f"El factorial de {num} es {valorFact}")

