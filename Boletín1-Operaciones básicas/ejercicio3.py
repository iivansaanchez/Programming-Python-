'''
Created on 20 sept 2022

@author: ivansanchezsanchez
'''


#Debe ser Verdadera si el contenido de la variable entera precio es igual o 
#superior a 60 euros pero igual o inferior a 420 euros.
precio = int(input("Introduce un precio: "))
if precio >= 60 and precio <= 420:
    precio = True 
else:
    precio = False 
print(precio)

     

#Debe ser Verdadera si el numero contenido en la variable entera numero es impar.
numero = int(input("Introduce un número: "))
if numero%2 == 0:
    numero = True 
else:
    numero = False 
print(numero)

#Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son válidas.
saldoCuenta = int(input("Introduce saldo en cuenta: "))
dineroSacar = int(input("Introduce cantidad de dinero a retirar: "))

if saldoCuenta >= dineroSacar:
    dineroSacar = True 
else:
    dineroSacar = False 
print(dineroSacar)

#Debe ser Verdadera si las variables enteras hora y minutos son correctas, 
#es decir, que estén comprendidas entre 0:0 y 23:59.

hora = int(input("Introduce una hora: "))
minuto = int(input("Introduce unos minutos: "))
resultado1 = True 

if 0 >= hora <= 24 and 0 >= minuto <= 59:
    resultado1
else:
    resultado = False 
print(resultado1)

#Debe ser Verdadera si la variable estadoCivil que almacena el 
#estado civil de una persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).

estadoCivil = input("Introduce tu estado civil (S-Soltero, C-Casado, V-Viudo, D-Divorciado): ")
resultado2 = True 

if estadoCivil == "S" or estadoCivil == "C" or estadoCivil == "V" or estadoCivil == "D":
    resultado2
else:
    resultado = False 
print(resultado2)


























    

