––'''
Created on 14 nov 2022

@author: ivansanchezsanchez
'''
'''
Escribir una función denominada encajan que indique si dos fichas 
de dominó encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente formato
[3,4] [2,5]
'''
listaPieza1=[5,3]
listaPieza2=[2,4]

def encajan(listaPiezas1, listaPiezas2):
    encajan = True
    if listaPieza1[0] == listaPiezas2[0] or listaPiezas1[1] == listaPiezas2[0] or listaPiezas1[0] == listaPiezas2[1] or listaPiezas1[1] == listaPiezas2[1]:
        encajan=encajan
    else:
        encajan = False

    return encajan

print(encajan(listaPieza1, listaPieza2))
