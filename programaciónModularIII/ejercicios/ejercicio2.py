'''
Created on Nov 28, 2022

@author: estudiante
'''
'''
Design a function called lowCaseInString that has a string of characters as parameter,
the method should return how many of those characters are lowercase letters.
'''
string=("Pepacomemuchaspipas")

def lowCaseInString(characterString):
    contador = 0
    for i in range(len(characterString)):
        if characterString[i] == characterString[i].lower():
            contador+=1
    return contador

print(lowCaseInString(string))