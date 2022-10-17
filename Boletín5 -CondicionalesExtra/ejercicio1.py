'''
Created on 17 oct 2022

@author: ivansanchezsanchez

Escribe el código de un programa que reciba un número de nota de 0 a 100 y nos informe de las calificaciones en el siguiente formato:
90-100, Sobresaliente 70-89, Notable
60-69, Bien
50-59, Suficiente 0-49, Suspenso
'''

nota = int(input("Introduce una nota (0-100): "))

if 0 < nota < 100:
    if 0 <nota < 49:
        print(f"Tú nota es {nota} SUSPENSO")
    elif 50 < nota < 59:
        print(f"Tú nota es {nota} SUFICIENTE")
    elif 60 < nota < 69:
        print(f"Tú nota es {nota} BIEN")
    elif 70 < nota < 89:
        print(f"Tú nota es {nota} NOTABLE")
    else:
        print(f"Tú nota es {nota} SOBRESALIENTE")
