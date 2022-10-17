'''
Created on Sep 29, 2022

@author: estudiante
'''

#En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
#porcentaje de rebaja que se aplicará sobre el precio original del producto se
#calcula de la siguiente forma:

#Si el producto es de tipo A, independientemente de su precio se
#aplica un 7% de descuento.

#Si el producto es de tipo C o bien el precio es inferior a 500€ se
#aplicará un porcentaje del 12% de descuento.

#En el resto de casos se aplica un 9% de descuento.


#Realizar un programa que solicite los datos necesarios (tipo de producto y
#precio original) y calcule el precio rebajado. Debe comprobarse que los
#datos de entrada son correctos, y si no lo son mostrar un mensaje de error.

tipoProducto = input("Introduce el tipo de producto A, B o C: ")
precioOriginal = int(input("Introduce su precio original: "))

if tipoProducto == "A" and precioOriginal >= 0:
    precioFinal = (precioOriginal * 7)/100
    print("El descuento es de: %s €"(precioFinal))
elif tipoProducto == "C" or precioOriginal < 500 and precioOriginal >= 0:
    precioFinal = (precioOriginal * 12)/100
    print("El descuento es de: %s €"(precioFinal))
elif precioOriginal>=0:
    precioFinal = (precioOriginal*9)/100
    print("El descuento es de: %s €"(precioFinal))
else:
    print("Los valores introducidos son erroneos")
    