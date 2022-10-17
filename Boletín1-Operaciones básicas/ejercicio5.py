'''
Created on 20 sept 2022

@author: ivansanchezsanchez
'''

A=True 
B=True 

#(A OR B) AND NOT(A)
print((A or B) and not (A))
#NOT(A OR B) AND B
print(not(A or B) and B)
#A OR NOT (B)
print(A or not (B))
#NOT((A AND B) AND (B OR A))
print(not((A and B) and (B or A)))

A1=True 
B1=False 

#(A OR B) AND NOT(A)
print((A1 or B1) and not (A1))
#NOT(A OR B) AND B
print(not(A1 or B1) and B1)
#A OR NOT (B)
print(A1 or not (B1))
#NOT((A AND B) AND (B OR A))
print(not((A1 and B1) and (B1 or A1)))

A2=False 
B2=True 

#(A OR B) AND NOT(A)
print((A2 or B2) and not (A2))
#NOT(A OR B) AND B
print(not(A2 or B2) and B2)
#A OR NOT (B)
print(A2 or not (B2))
#NOT((A AND B) AND (B OR A))
print(not((A2 and B2) and (B2 or A2)))

A3=False 
B3=False 

#(A OR B) AND NOT(A)
print((A3 or B3) and not (A3))
#NOT(A OR B) AND B
print(not(A3 or B3) and B3)
#A OR NOT (B)
print(A3 or not (B3))
#NOT((A AND B) AND (B OR A))
print(not((A3 and B3) and (B3 or A3)))

