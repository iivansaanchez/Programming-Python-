'''
Created on 25 oct 2022

@author: ivansanchezsanchez

Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si 
el año es impar su familia le regala un puzzle; si es par, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles obtiene el 
doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una edad determinada 
sabiendo que en el primer cumpleaños le regalaron un puzzle y en el segundo 20€.
'''

puzle = 0
dinero = 0
año = int(input("Introduce un número de años: "))
contador = año
while año <= 0:
    año = int(input("Año inválido. Introduce un número de años: "))

if año >= 1:
    puzle += 1
    
if año >= 2:
    dinero += 20

acumuladorPuzle=puzle
recibe=dinero
while año > 2:
    if año%2==0:
        recibe = recibe + 15
        dinero += recibe
    elif año%2!=0:
        puzle+=acumuladorPuzle+1
        puzle = acumuladorPuzle
    año-=1
print(f"Tenemos {puzle} puzles y {dinero}€")