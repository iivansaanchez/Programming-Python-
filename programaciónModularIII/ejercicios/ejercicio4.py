'''
Created on Nov 28, 2022

@author: estudiante
'''
'''
Design a function called numberInString that receives a string of characters as
parameter and returns how many of them are numbers.
'''

string=("p1p4")


def numberInString(characterString):
    contador=0
    numberString = "0123456789"
    for a in range(len(characterString)):
        for i in range(len(numberString)):
            if characterString[a] == numberString[i]:
                contador+=1
    return contador

print(numberInString(string))