'''
Created on 31 oct 2022

@author: ivansanchezsanchez

Triángulos. Escribe un programa que pida un número y a continuación pinte un triángulo 
como los siguientes utilizando el número como símbolo.
'''
cadenaNum=""
num = int(input("Introduce un número: "))
while num <= 0:
    num = int(input("El valor no es válido. Introduce otro número: "))
    
for i in range(1, num+1):
    cadenaNum=str(num)*i
    print(cadenaNum)
