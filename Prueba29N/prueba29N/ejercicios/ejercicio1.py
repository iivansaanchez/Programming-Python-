'''
Created on Nov 29, 2022

@author: estudiante
'''

def generar_usuario(nombre, apellido1, apellido2, dni):
    usuario=""
    a=0
    b=-1
    c = 0
    d = -2
    while a < 3:
        usuario+=nombre[a]
        a+=1
    while b > -4:
        usuario+=apellido1[b]
        b-=1
    while c < 3:
        usuario+=apellido2[c]
        c+=1
    while d > -6:
        usuario+=dni[d]
        d-=1     
    return usuario
def menu():
    print("1. Añadir usuario válido")
    print("2. Eliminar usuario.")
    print("3. Crear usuario.")
    print("4. Consultar usuario.")
    print("5. Borar usuario.")
    print("6. Salir")

nombrep = input("Introducir nombre: ")
apellido1p = input("Introducir apellido1: ")
apellido2p = input("Introducir apellido2: ")
dnip = input("Introducir dni: ")
print(menu())
number = int(input("Introduce un número: "))
while number < 6:
    if number == 1:
        listaUsuarios=["", "", "", "", ""]
        contadorA = 0
        if contadorA < 5:
            listaUsuarios[contadorA]+=generar_usuario(nombrep, apellido1p, apellido2p, dnip)
            contadorA+=1
            number = int(input("Introduce un número: "))
        else:
            contadorA=0
            number = int(input("Introduce un número: "))
    elif number == 2:
        usuarioD=input("Introduce el nombre del usuario que deseas eliminar: ")
        for i in range(len(listaUsuarios)):
            for a in usuarioD:
                if usuarioD[a]==listaUsuarios[i]:
                    listaUsuarios[i]=""
    
    elif number == 3:
        nombrep = input("Introducir nombre: ")
        apellido1p = input("Introducir apellido1: ")
        apellido2p = input("Introducir apellido2: ")
        dnip = input("Introducir dni: ")
        
        if contadorA < 5:
            listaUsuarios[contadorA]+=generar_usuario(nombrep, apellido1p, apellido2p, dnip)
            contadorA+=1
        else:
            contadorA=0
            
    number = int(input("Introduce un número: "))
    nombrep = input("Introducir nombre: ")
    apellido1p = input("Introducir apellido1: ")
    apellido2p = input("Introducir apellido2: ")
    dnip = input("Introducir dni: ")
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        