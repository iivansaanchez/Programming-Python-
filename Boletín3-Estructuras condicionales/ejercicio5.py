'''
Created on Sep 26, 2022

@author: estudiante
'''

#Realizar un programa que solicite 4 números e imprima la media de los
#números. También debe imprimir aquellos números que son superiores a la
#media

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce un número: "))
numero3 = int(input("Introduce un número: "))
numero4 = int(input("Introduce un número: "))

realizarMedia = (numero1 + numero2 + numero3 + numero4)/4
print(realizarMedia)

if numero1 > realizarMedia:
    print("Es mayor que la media el número %s" %(numero1))
if numero2 > realizarMedia:
    print("Es mayor que la media el número %s" %(numero2))
if numero3 > realizarMedia:
    print("Es mayor que la media el número%s" %(numero3))
if numero4 > realizarMedia:
    print("Es mayor que la media el número %s" %(numero4))