'''
Connor Kissack
Pseudo to Python
March 8, 2021
'''


N = [2, 9, 5, 6, 7, 8]
X = 7
Found= False
Counter = 0
for counter in range(6):
    if N[Counter] == X:
        Found = False
    print (N[Counter],"found at position")

if Found == False:
    print(X,"not found")




