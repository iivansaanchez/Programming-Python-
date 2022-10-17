'''
Created on Oct 11, 2022

@author: estudiante

Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format
'''

number = int(input("Enter one number between 0 and 10: "))

if 0 <= number <= 10:
    print("El número es válido.")
    print("La tabla de múltiplicación del número %s es: " %(number))
    for i in range (0, 11):
        print(i * number)
else:
    print("The number is out of the boundaries")
    
    

