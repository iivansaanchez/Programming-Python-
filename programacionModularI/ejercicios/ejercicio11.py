'''
Created on Nov 23, 2022

@author: estudiante
'''
'''
Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno
'''
lista1=[1, 2, 3, 4, 5]
lista2=[4, 5, 6, 7, 8]

def intersect(lista1, lista2):
    elementosComunes=[]
    for i in range(len(lista1)):
        for a in range(len(lista2)):
            if lista1[i] == lista2[a]:
                elementosComunes.append(lista1[i])
    return elementosComunes

print(intersect(lista1, lista2))