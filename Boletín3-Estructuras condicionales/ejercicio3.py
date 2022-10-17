'''
Created on Sep 26, 2022

@author: estudiante
'''

#Realizar un programa que lea un número por teclado. El programa debe
#imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
#mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
#deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
#el programa finaliza sin mostrar ningún mensaje.

numero = int(input("Introduce un número: "))
if numero % 2 == 0 and numero % 3 == 0:
    print("El número es multiplo de 2 y 3.")
elif numero % 2 == 0:
    print("El número es múltiplo de 2.")
elif numero % 3 == 0:
    print("El número es mĺtiplo de 3.")
else:
    print()
    
