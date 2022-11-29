'''
Created on Nov 28, 2022

@author: estudiante
'''

'''
Design a function called charactersInString that has a character string and a character
as input parameters and returns how many times that character appears in the string. It
should do it no matter if the string and character are lower case or upper case characters.
'''
string = "PEPA COME MUCHAS PIPAS".upper()
char = "P".upper()
def charactersInString(characterString, character):
    contador=0
    for i in range(len(characterString)):
        if characterString[i] == character:
            contador+=1
    return contador

print(charactersInString(string, char))
