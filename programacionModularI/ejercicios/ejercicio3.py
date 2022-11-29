'''
Created on Nov 10, 2022

@author: estudiante
'''

def es_bisiesto(year):
    
    return year%4==0 and (year%100!=0 or year%400==0)



def tranformarLargo(dd, mm, yyyy):
    nombreMeses= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if 1<=mm<=12 and ((1 <= dd <= dias[mm-1]) or (es_bisiesto(yyyy) and 1<=dd<=29 and dias[mm-1])):
        
        mensaje = f"{dd} de {nombreMeses[mm-1]} de {yyyy}"
    else:
        mensaje = "La fecha introducida no es válida."
        
     
    return(mensaje)

day = int(input("Introduce un dia: "))
month = int(input("Introduce un mes: "))
year = int(input("Introduce un año: "))

while day >= 0:
    print(tranformarLargo(day, month, year))
    
    day = int(input("Introduce un dia: "))
    month = int(input("Introduce un mes: "))
    year = int(input("Introduce un año: "))





