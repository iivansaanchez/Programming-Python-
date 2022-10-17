'''
Created on Sep 27, 2022

@author: estudiante
'''

#Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
#Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
#pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
#siguientes reglas:moodle cnetores

estadoCivil = input("¿Cuál es tu estado civil S-Soltero, C-Casado, V-Viudo y D-Divorciado ?:")
edad = int(input("¿Cuá es tu edad?"))

if estadoCivil == "S" or (estadoCivil == "D" and edad < 35):
    print("Se le retiene un 12%")
elif edad > 50:
    print("Se le retiene un 8.5%")
elif estadoCivil == "V" or (estadoCivil == "C" and edad < 35):
    print("Se le retiene un 11,3%")
else:
    print("Se le retiene un 10,5%")
    
    
    