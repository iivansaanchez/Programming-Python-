'''
Created on 25 oct 2022

@author: ivansanchezsanchez

La secuencia siguiente está definida para el conjunto de los números enteros:
n → n/2 (n es par)
n → 2n + 1 (n es impar)
Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia de números:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
 Elabora un programa que pida un número n e imprima una cadena con la secuencia 
 de números hasta llegar a 1.
'''
numeroN = int(input("Introduce un número: "))
while numeroN <= 0:
    numeroN = int(input("El número no es válido. Introduce otro número: "))
listaPares = ""
listaImpares = ""

for i in range(numeroN, 0, -1):
    if i%2==0:
        listaPares+=str(i)
        if i!=1:
            listaPares+="→"
    elif (2*i+1)%3==1:
        listaImpares+=str(i)
        if i!=1:
            listaPares+="→"
print(listaPares)
print(listaImpares)