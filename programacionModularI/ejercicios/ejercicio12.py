'''
Created on Nov 24, 2022

@author: estudiante
'''
'''
Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).
'''

lista=[1, 2, 3, 4, 5]
lista2=[9, 8, 7, 6, 5]
def unionListas(listaPrincipal, listaSecundaria):
    listaConjunto=[] 
    for i in range(len(lista)):
        if lista[i]!=lista2[i]:
            listaConjunto.append(lista[i])
            listaConjunto.append(lista2[i])    
    return listaConjunto


print(unionListas(lista, lista2))   