'''
Created on Nov 4, 2022

@author: estudiante
'''

from random import randint
lista=[]
for i in range(10):
    num = randint(0, 100)
    lista.append(num)
print(lista)
def menu():
    print("a. Conocer el mayor")
    print("b. Conocer el menor")
    print("c. Obtener la suma de todos los números")
    print("d. Obtener la media")
    print("e. Sustituir el valor de un elemento por otro número introducido por teclado")
    print("f. Mostrar todos los números")
print(menu())
def obtenerElementoMayor(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def obtenerElementoMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def obtenerSumaNumero(lista):
    suma=0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def obtenerMediaNumero(lista):
    suma=0
    for i in range(len(lista)):
        suma += lista[i]
    media = suma/len(lista)
    return media

def mostrarTodosLosNumero(lista):
    print(lista)
    
numeroSustituir = int(input("Introduce un numero a sustituir: "))
valorCambio = int(input("Introduce un valor de cambio: "))
def sustitucionElemento(lista, ns, vc):
    for i in range(len(lista)):
        if ns==lista[i]:
            lista[i] = vc
    return lista

opcion = input("Introduce una opcion (a, b, c ,d, e, f): ").upper()
while opcion != "A" or opcion != "B" or opcion != "C" or opcion != "D" or opcion != "E" or opcion != "F":
    opcion = input("Valor introducido no válido. Introduce una opcion (a, b, c ,d, e, f): ").upper()
    
while opcion != "G":
    print(menu())
    if opcion == "A":
        print(obtenerElementoMayor(lista))
    elif opcion =="B":
        print(obtenerElementoMenor(lista))
    elif opcion == "C":
        print(obtenerSumaNumero(lista))
    elif opcion == "D":
        print(obtenerMediaNumero(lista))
    elif opcion == "E":
        print(sustitucionElemento(lista, numeroSustituir, valorCambio))

