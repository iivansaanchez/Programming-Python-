'''
Created on Nov 28, 2022

@author: estudiante
'''
'''
Design a function called upperCaseInString that has a string of characters as parameter
and the method should return how many are uppercase letters.
'''

string = "PepaComeMuchasPipas"

def upperCaseInString(characterString):
    contador=0
    for i in range(len(characterString)):
        if characterString[i] == characterString[i].upper():
            contador += 1
            
    return contador

print(upperCaseInString(string))