'''
Created on Sep 22, 2022

@author: estudiante
'''

#Escribir una expresión lógica que cumpla:
#Debe ser Verdadera si el contenido de las variables enteras 
#sueldo_bruto y sueldo_neto es el adecuado para una retención del 22%.

sueldo_bruto = int(input("Introduce tu sueldo bruto: "))
sueldo_neto = int(input("Introduce sueldo neto: "))
retencion = (sueldo_bruto * 22)/100
resultado = True

if sueldo_neto >= retencion:
    resultado
else:
    resultado = False 
print(resultado)


#Debe ser Verdadera si el contenido de la variable entera día es un valor válido para el mes
#de mayo.

dia = int(input("Introduce un día para el mes de Mayo: "))
resultado =  True

if dia >=1 and dia <=31:
    resultado
else: 
    resultado = False 
print(resultado)

#Debe ser Verdadera si el número contenido en las variables enteras num1 y num2 son
#múltiplos de tres

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
resultado= True 

if num1%3 == 0 and num2%3 == 0:
    resultado 
else:
    resultado = False 
print(resultado)

#Debe ser Verdadera si la calificación contenida en la variable real nota es un aprobado.

nota = int(input("Intoduce tu nota: "))
resultado = True 

if nota >= 5:
    resultado 
else:
    resultado = False 
print(resultado)

#Debe ser Verdadera si la media de la calificación contenida en las variables reales nota1,
#nota2 y nota3 es un aproblado

nota1 = int(input("Introduce tu nota de Programación: "))
nota2 = int(input("Introduce la nota de Base de datos: "))
nota3 = int(input("Introduce la nota de Lenguaje de Marcas: "))
notaMedia = (nota1 + nota2 + nota3)
resultado = True 

if notaMedia >= 5 and nota <= 10:
    resultado
else:
    resultado = False 
print(resultado)


