'''
Created on Sep 22, 2022

@author: estudiante
'''

#Escribir una expresión lógica que cumpla:
#Debe ser Falsa si alguna de las calificaciones contenidas en las variables reales nota1, nota2
#y nota3 es un suspenso.

nota1 = int(input("Introduce tu nota de Programación: "))
nota2 = int(input("Introduce la nota de Base de datos: "))
nota3 = int(input("Introduce la nota de Lenguaje de Marcas: "))
resultado = True 

if nota1 >= 5 and nota2 >= 5 and nota3 >= 5:
    resultado 
else:
    resultado = False 
print(resultado)

#Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga menos de
#1000 euros en la variable saldo o se haya quedado al descubierto más de 5 veces. Este
#último dato se almacenará en la variable descubierto

saldo = int(input("Introduce tu saldo: "))
descubierto = int(input("Introduce las veces que has quedado al descubierto: "))
resultado = True 

if saldo < 1000 or descubierto > 5:
    resultado 
else:
    resultado = False 
print(resultado)


#Debe ser Falsa cuando el valor almacenado en la variable asignaturasAprobadas sea
#inferior al 30% del valor almacenado en la variable asignaturasCurso.

asignaturasAprobadas = int(input("Introduce el número de asignaturas que has aprobado: "))
asignaturasCurso = int(input("Introducir el número de asignaturas: "))
porcentajeAprobado = (asignaturasCurso*30)/100
resultado = True 

if porcentajeAprobado < asignaturasAprobadas:
    resultado
else:
    resultado = False
print(resultado)

#Debe ser Falsa si los números contenido en las variables enteras mes y día no son válidos.
#Vamos a considerar que no hay años bisiestos.

dia = int(input("Introduce un dia del mes: "))
mes = input("Introduce un mes: ")
resultado = True

if dia >=1 and dia <=28 and mes == "Febrero":
    resultado
    
elif dia >=1 and dia <=30 and mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
    resultado
        
elif dia >=1 and dia <=31 and mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
    resultado
    
else:
    resultado = False
    
























