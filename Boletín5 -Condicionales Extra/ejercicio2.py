'''
Created on 17 oct 2022

@author: ivansanchezsanchez
Escribe una aplicación que pida la fecha actual (día y mes) y 
el hemisferio (Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21 diciembre), 
Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), 
Verano (desde 21 diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio).
'''

dia = int(input("Introduce un dia del mes: "))
mes = int(input("Introduce un mes del año: "))



emisferio = input("En que emisferio te encuentras: ").upper()

if dia > 0 and 1 <= mes <=12:
    if emisferio == "NORTE" or emisferio == "SUR":
        if emisferio == "NORTE":
            if (23 < dia < 30 and mes == 9) or (1 < dia < 31 and mes == 10) or (1 < dia < 30 and mes == 11) or (1 < dia < 20 and mes == 12):
                print(f"En el emisferior {emisferio} es OTOÑO")  
            elif (21 < dia < 31 and mes == 12) or (1 < dia < 31 and mes == 1) or ((1 < dia < 28 or 1 < dia < 29) and mes == 2) or (1 < dia < 20 and mes == 3):
                print(f"En el emisferior {emisferio} es INVIERNO")
            elif (21 < dia < 31 and mes == 3) or (1 < dia < 30 and mes == 4) or (1 < dia < 31 and mes == 5) or (1 < dia < 20 and mes == 6):
                print(f"En el emisferior {emisferio} es PRIMAVERA") 
            else:
                print(f"En el emisferior {emisferio} es VERANO")    
        else:
            if (23 < dia < 30 and mes == 9) or (1 < dia < 31 and mes == 10) or (1 < dia < 30 and mes == 11) or (1 < dia < 20 and mes == 12):
                print(f"En el emisferior {emisferio} es PRIMAVERA")  
            elif (21 < dia < 31 and mes == 12) or (1 < dia < 31 and mes == 1) or ((1 < dia < 28 or 1 < dia < 29) and mes == 2) or (1 < dia < 20 and mes == 3):
                print(f"En el emisferior {emisferio} es VERANO")
            elif (21 < dia < 31 and mes == 3) or (1 < dia < 30 and mes == 4) or (1 < dia < 31 and mes == 5) or (1 < dia < 20 and mes == 6):
                print(f"En el emisferior {emisferio} es OTOÑO") 
            else:
                print(f"En el emisferior {emisferio} es INVIERNO")
    else:
        print("Los valores introducidos no son válidos.")                                                               
else:
    print("Los valores introducidos no son válidos.")       
