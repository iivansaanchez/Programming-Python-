'''
Created on 17 nov 2022

@author: ivansanchezsanchez
'''

listaNum=[1, 2, 3, 4, 5]

def listaMenores(lista, k):
    listaMenores=[]
    for i in range(len(lista)):
        if lista[i]<k:
            listaMenores.append(lista[i])
    return listaMenores

def listaMayores(k, num):
    listaMayores=[]
    for i in range(k, num+1):
        listaMayores.append(i)
    return listaMayores

def listaMultiplos(k, num):
    listaMultiplos=[]
    for i in range(1, num+1):
        listaMultiplos.append(k*i)
    return listaMultiplos


print(listaMenores(listaNum, 5))
print(listaMayores(5, 10))
print(listaMultiplos(5, 5))