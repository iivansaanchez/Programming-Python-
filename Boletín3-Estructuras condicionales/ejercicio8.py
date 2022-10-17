'''
Created on Sep 29, 2022

@author: estudiante
'''

#Realizar un programa que lea por teclado dos marcaciones de un reloj
#digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
#23:59:59 e informe cual de ellas es mayor.

hora1, minuto1, segundos1 = 20, 20, 20
hora2, minuto2, segundos2 = 20, 20, 20

if  (0<=hora1<=23 or 0<=minuto1<=59 or 0<=segundos1<=59) and (0<=hora2<=23 or 0<=minuto2<=59 or 0<=segundos2<=59):
    
    if hora1 > hora2:
        print("La hora 1 es mayor que la hora 2: %s:%s:%s > %s:%s:%s"%(hora1, minuto1, segundos1, hora2, minuto2, segundos2))
    elif hora1 < hora2:
        print("La hora 1 es menor que la hora 2: %s:%s:%s < %s:%s:%s"%(hora1, minuto1, segundos1, hora2, minuto2, segundos2))
    else:
        if minuto1 > minuto2 :
            print("Los minutos de la hora 1 son mayores que los de la hora 2: %s:%s:%s < %s:%s:%s"(hora1, minuto1, segundos1, hora2, minuto2, segundos2))
        elif minuto1 > minuto2 :
            print("Los minutos de la hora 1 son menores que los de la hora 2: %s:%s:%s < %s:%s:%s"(hora1, minuto1, segundos1, hora2, minuto2, segundos2))
        else:
            if segundos1 > segundos2 :
                print("Los segundos de la hora 1 son mayores que los segundos de la hora 2: %s:%s:%s < %s:%s:%s"(hora1, minuto1, segundos1, hora2, minuto2, segundos2))
            elif segundos1 < segundos2 :
                print("Los segundos de la hora 1 son menor que los segundos de la hora 2: %s:%s:%s < %s:%s:%s"(hora1, minuto1, segundos1, hora2, minuto2, segundos2))
            else:
                print("Las horas son iguales.")
else:
    print("Los datos introducidos son erroneos.")
            
            
            
            
            
            
            
            
            
            