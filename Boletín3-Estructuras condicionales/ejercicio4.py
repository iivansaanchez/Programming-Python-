'''
Created on Sep 26, 2022

@author: estudiante
'''


#Realizar un programa que lea la edad de una persona menor a 100 años e
#informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
#29) o un adulto.

edad = int(input("Introduce tu edad: "))

if 0 <= edad <= 12 and edad < 100:
    print("Eres un niño/a/e.")
elif 13 <= edad <= 17 and edad < 100:
    print("Eres un adolescente.")
elif 18 <= edad <= 29 and edad < 100:
    print("Eres joven.")
elif edad >= 30 and edad < 100:
    print("Eres un/a adulto/a")
else:
    print("El valor introducido no es válido")
    