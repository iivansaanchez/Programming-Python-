'''
Created on 31 oct 2022

@author: ivansanchezsanchez
Escribe un programa que pregunte por el tipo de figura que quiere pintar y el tamaño 
del lado de la figura y genere las figuras correspondientes en el siguiente formato 
(los valores 3, 4 y 5 son de ejemplo, podrían pedirse desde 1 hasta 10).
'''

num=3#int(input("Introduce numero: "))
print("a. Cuadrados")
secuencia=""
for i in range(1, num+1):
    secuencia=(num*" * ")
    
    print(secuencia)
num=3#int(input("Introduce numero: "))
print("b. Triangulos")
for i in range(1, num+1):
    num-=1
    i=i+i
    if i!=1:
        i+=1
    print((" "*num)+(i-2)*"*")
num=3#int(input("Introduce numero: "))
print("c. Rombos")
for i in range(1, num+num):
    if num>(num//2):
        num-=1
        i=i+i
        if i!=1:
            i+=1
        print((" "*(num))+(i-2)*"*")

