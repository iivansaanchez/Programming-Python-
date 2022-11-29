'''
Created on 14 nov 2022

@author: ivansanchezsanchez
'''
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def moverDerecha(lista):
    nuevaLista=[]
    for i in range(len(lista)):
        nuevaLista.append(lista[i-1])
    return nuevaLista
print(moverDerecha(lista))