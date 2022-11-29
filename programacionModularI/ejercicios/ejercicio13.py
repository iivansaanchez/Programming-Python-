'''
Created on Nov 25, 2022

@author: estudiante
'''

'''
Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
'''

listaNombre = ["Alvaro", "Andres", "Abril", "Enrique", "Eustaquia", "Daniel"]

def devolverNombre(lista, letra):
    listaNombres=[]
    for i in range(len(lista)):
        if lista[i][0].lower() == letra.lower():
            listaNombres.append(lista[i])
            
    return listaNombres

print(devolverNombre(listaNombre, "A"))