'''
Created on 20 sept 2022

@author: ivansanchezsanchez
'''

#Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
#es superior a 300 euros o negativa.

cantidadSacar = int(input("Introducir cantidad a sacar: "))
resultado = True

if cantidadSacar >= 0 and cantidadSacar <= 300:
    resultado
else:
    resultado = False 
print(resultado) 

#Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22
#años.

edad = int(input("Introduce una edad: "))
resultado1 = True 

if 16 >= edad <=22:
    resultado1 
else:
    resultado1 = False 
print(resultado1)

# Debe ser Falsa si; la variable respuesta a una pregunta de tipo (S/N), es válida.


respuesta = input("Estudias 1ºDAW en Brenes: ")
respuesta1 = input("¿Qué edad tienes?: ")
resultado2 = False

if respuesta == "Si" or respuesta == "No" and respuesta1 == "Si" or respuesta1 == "No":
    resultado2 
else:
    resultado2 = True 
print(resultado2)

#Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.

numero = int(input("Introduce un número: "))
resultado3 = False 

if numero%7 == 1 or numero%3 == 1:
    resultado3 
else:
    resultado3 = True 
print(resultado3)


    







    