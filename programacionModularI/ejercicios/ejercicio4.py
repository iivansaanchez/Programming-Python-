'''
Created on 14 nov 2022

@author: ivansanchezsanchez
'''

lista = []
num = int(input("Introduce un número para añadir a la lista: "))
lista.append(num)
        
while num > 0:
    num = int(input("Introduce un número para añadir a la lista: "))
    lista.append(num)

def obtenerElementoMayor(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def obtenerNumeroPares(lista):
    listaPares=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            listaPares.append(lista[i])
    return listaPares

print(obtenerElementoMayor(lista))
print(obtenerNumeroPares(lista))
            
