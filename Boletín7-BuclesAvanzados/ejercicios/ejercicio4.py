'''
Created on 25 oct 2022

@author: ivansanchezsanchez
Diseña un programa que reciba el tamaño de una secuencia numérica y 
muestre en una única línea cada una de las siguientes secuencias. 
Si se recibe el número 6 se imprimiría:
a. 1, -5, 25, -125, 625, -3125 
b. 1,-1,0,1,-1,0
c. 1, 3, 9, 27, 81, 243
'''
cadena1 = ""
cadena2 = ""
cadena3 = ""
num = int(input("Introduce un número: "))
while num <= 0:
    num = int(input("Número incorrecto. Introduce otro número: "))
for i in range(num):
    cadena1+=str((-5)**i)
    cadena2+=str((i%-3)+1)
    cadena3+=str(3**i)
    if i!=num-1:
        cadena1+=", "
        cadena2+=", "
        cadena3+=", "
print(cadena1)
print(cadena2)
print(cadena3)


