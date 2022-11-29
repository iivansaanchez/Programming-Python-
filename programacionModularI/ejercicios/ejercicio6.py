'''
Created on 14 nov 2022

@author: ivansanchezsanchez
'''
'''
Diseña una función llamada estaOrdenada que reciba una lista de elementos y 
devuelva True si está ordenada o False en caso contrario.
'''


lista=[1, 2, 3, 4, 6, 5, 7, 8, 9, 10]

def estaOrdenada(lista):
    ordenada = True
    numero1=lista[0]
    numero2=lista[1]
    for i in range(2, len(lista)):
        if numero1 < numero2:
            numero1 = numero2
            numero2=lista[i]
        else:
            ordenada = False
    return ordenada
        
print(estaOrdenada(lista))
        