'''
Created on 14 nov 2022

@author: ivansanchezsanchez
'''

'''
Realiza un programa que añada números enteros a una lista hasta que se introduzca un número negativo. 
Haciendo uso de esta lista, elabora funciones que devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.
'''

lista=[1, 2, 3, 4, 5]

num=int(input("Introduce números para añadir a la lista: "))
while num>0:
    num=int(input("Introduce números para añadir a la lista: "))
  
def es_primo(num):
    esPrimo = True 
    if num > 2:
        for i in range(2, num):
            if num%i==0:
                esPrimo = False
    return esPrimo

for i in lista:
    print(i, es_primo(i))  
    
def sumatorio(lista):
    sumatorio = 0
    for i in range(len(lista)):
        sumatorio+=lista[i]
    return sumatorio

def mediaValores(lista):
    media = 0
    for i in range(len(lista)):
        media+=lista[i]
    media=media//(len(lista))
    return media

def factorialNumero(lista):
    listaFact=[]
    valorFact=1
    for i in range(1, len(lista)):
        valorFact=valorFact*i
        listaFact.append(valorFact)
    return listaFact


print(es_primo(num))
print(sumatorio(lista))
print(mediaValores(lista))
print(factorialNumero(lista))
print()
    