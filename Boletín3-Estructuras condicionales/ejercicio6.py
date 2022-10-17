'''
Created on Sep 26, 2022

@author: estudiante
'''
#Realizar un programa que solicite un carácter por teclado e informe por
#pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
#mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.

letra = input("Introduce una VOCAL: ")

if letra == ("A"):
    print("La letra introducida corresponde a la primera vocal: " + letra)
elif letra == ("E"):
    print("La letra introducida corresponde a la segunda vocal: " + letra)
elif letra == ("I"):
    print("La letra introducida corresponde a la tercera vocal: " + letra)
elif letra == ("O"):
    print("La letra introducida corresponde a la cuarta vocal: " + letra)
elif letra == ("U"):
    print("La letra introducida corresponde a la quinta vocal: " + letra)
else:
    print("El cáracter introducido no corresponde a ninguna vocal.")