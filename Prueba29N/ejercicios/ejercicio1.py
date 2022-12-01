'''
Created on 29 nov 2022

@author: ivansanchezsanchez
'''
def generar_usuario(nombre, apellido1, apellido2, dni):
    usuario=""
    usuario+=nombre[:3]
    usuario+=apellido1[-3:]
    usuario+=apellido2[:3]
    usuario+=dni[-5:-1]
    return usuario

def menu():
    mensaje = " 1. Añadir usuario válido. \n 2.Eliminar usuario. \n 3. Crear usuario. \n 4. Consultar usuarios. \n 5. Borrar usuarios. \n 6. Salir"
    
    return mensaje


nom=input("Introduce un nombre: ")  
ape1=input("Introduce un apellido1: ")
ape2=input("Introduce un apellido2: ")
dnip=input("Introduce un dni: ")

print(menu())

number=int(input("Elige una opción: "))

listaUsuarios=["", "", "", "", ""]

contadorA=0

while number!=6:
    print(menu())
    if number == 1:
        if contadorA <5:
            listaUsuarios[contadorA]+=generar_usuario(nom, ape1, ape2, dnip)
            contadorA+=1
        else:
            contadorA=0
            listaUsuarios[contadorA]+=generar_usuario(nom, ape1, ape2, dnip)
    elif number == 2:
        if generar_usuario(nom, ape1, ape2, dnip) in listaUsuarios:
            listaUsuarios.remove(generar_usuario(nom, ape1, ape2, dnip))
            listaUsuarios.append("")
            print(listaUsuarios)
        else:
            print("El usuario no se encuentra en la lista.")
    elif number == 3:
        nom=input("Introduce un nombre: ")  
        ape1=input("Introduce un apellido1: ")
        ape2=input("Introduce un apellido2: ")
        dnip=input("Introduce un dni: ")
        if contadorA <5:
            listaUsuarios[contadorA]+=generar_usuario(nom, ape1, ape2, dnip)
            contadorA+=1
        else:
            contadorA=0
            listaUsuarios[contadorA]+=generar_usuario(nom, ape1, ape2, dnip)
    elif number == 4:
        print(listaUsuarios)
    elif number == 5:
        listaUsuarios=["", "", "", "", ""]
    
    number=int(input("Elige una opción: "))
    if number == 1 or number == 2 or number == 3:      
        nom=input("Introduce un nombre: ")  
        ape1=input("Introduce un apellido1: ")
        ape2=input("Introduce un apellido2: ")
        dnip=input("Introduce un dni: ") 