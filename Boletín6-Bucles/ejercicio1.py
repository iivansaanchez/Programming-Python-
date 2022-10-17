'''
Created on Oct 11, 2022

@author: estudiante

Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.
'''

for i in range(101):
    if i%7 == 0 and i%13 == 0:
        print(i)
        print("El número es múltiplo de 7 y de 13")
    elif i%7 == 0:
        print(i)
        print("El número es múltiplo de 7")
    elif i%13 == 0:
        print(i)
        print("El número es múltiplo de 13")
    else:
        print(i)
