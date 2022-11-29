'''
Created on Nov 25, 2022

@author: estudiante
'''

'''
Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .
'''
lista = ["ABCDEFGHYJK"]
lista2 = ["ABCDEFG"]

def longitudLista(a, b):
    mensaje=""
    if len(a) == len(b):
        mensaje=(f"Las listas tienen la misma logitud.")
    elif len(a) > len(b):
        mensaje=(f"La lista mas larga es {lista}")
    else:
        mensaje=(f"La lista más larga es {lista2}")
    return mensaje

print(longitudLista(lista, lista2))