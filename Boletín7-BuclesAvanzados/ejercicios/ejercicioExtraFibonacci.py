'''
Created on 28 oct 2022

@author: ivansanchezsanchez
'''

num=int(input("Introducir cantidad de número Fibonnaci: "))
while num <= 0:
    num1=int(input("El número no es válido. Introducir cantidad de número Fibonnaci: "))

primerNum = 0
segundoNum = 0
contadorSuma = 0
cadenaFibo = ""
#contador = 0

if num >= 1:
    primerNum = 1
    contadorSuma=primerNum
    #print(contadorSuma)
    cadenaFibo+=str(contadorSuma)
if num >= 2:
    segundoNum = 1
    contadorSuma = segundoNum
    #print(contadorSuma)
    cadenaFibo+=", "+str(contadorSuma)
for i in range(2, num):
    contadorSuma = primerNum + segundoNum
    primerNum = segundoNum
    segundoNum = contadorSuma
    #print(contadorSuma)
    cadenaFibo+=", "+str(contadorSuma)
print(cadenaFibo)
"""
while contador < num:
    contadorSuma = primerNum + segundoNum
    primerNum = segundoNum
    segundoNum = contadorSuma
    print(contadorSuma)
    contador+=1
 """   
