'''
Created on 17 oct 2022

@author: ivansanchezsanchez

Crea un programa que dada una fecha en formato 
(dd-mm-yyyy), nos devuelva cuántos días han 
transcurrido desde el 1 de enero de ese mismo año 
(considera que puede tratarse de un año bisiesto).
'''

dia, mes, año = (15, 7, 2007)
contadorDias = 0
if 1 <= mes <= 12 and 1 <= dia <= 31:
    if año%4==0:
        if (mes >= 1 or mes >= 3 or mes >= 5 or mes >= 7 or mes >= 8 or mes >= 10 or mes >= 12):
            if mes >= 1:
                if mes == 1:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 3:
                if mes == 3:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 5:
                if mes == 5:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 7:
                if mes == 7:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 8:
                if mes == 8:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 10:
                if mes == 10:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 12:
                if mes == 12:
                    contadorDias += dia
                else:
                    contadorDias += 31    
        if mes >= 2 and dia <=29:
            contadorDias += 29
        if mes >= 4 or mes >= 6 or mes >= 9 or mes >= 11 and dia<=30:
            if mes >= 4:
                if mes == 4 and 1 < dia < 30:
                    contadorDias += dia
                else:
                    contadorDias += 30
            if mes >= 6:
                if mes == 6 and 1 < dia < 30:
                    contadorDias += dia
                else:
                    contadorDias += 30
            if mes == 9:
                if mes == 9 and 1 < dia < 31:
                    contadorDias += dia
                else:
                    contadorDias += 30
            if mes >= 11:
                if mes == 11 and 1 < dia < 30:
                    contadorDias += dia
                else:
                    contadorDias += 30
            
    else:
        if mes >= 1 or mes >= 3 or mes >= 5 or mes >= 7 or mes >= 8 or mes >= 10 or mes >= 12:
            if mes >= 1:
                if mes == 1:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 3:
                if mes == 3:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 5:
                if mes == 5:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 7:
                if mes == 7:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 8:
                if mes == 8:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 10:
                if mes == 10:
                    contadorDias += dia
                else:
                    contadorDias += 31
            if mes >= 12:
                if mes == 12:
                    contadorDias += dia
                else:
                    contadorDias += 31 
        if mes >= 2 and dia <= 28:
            contadorDias += 28
        if mes >= 4 or mes >= 6 or mes >= 9 or mes >= 11 and dia <=30:
            if mes >= 4:
                if mes == 4:
                    contadorDias += dia
                else:
                    contadorDias += 30
            if mes >= 6:
                if mes == 6:
                    contadorDias += dia
                else:
                    contadorDias += 30
            if mes == 9:
                if mes == 9:
                    contadorDias += dia
                else:
                    contadorDias += 30
            if mes >= 11:
                if mes == 11:
                    contadorDias += dia
                else:
                    contadorDias += 30
        
else:
    print("Los valores introducidos no son válidos.")
    
print(contadorDias)
            
            
            
            
            