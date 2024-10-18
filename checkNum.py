#Python Exercise
'''
35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
'''

#Solution

def checkNum(x,y) :

    if x == y :
        return True
    
    elif x - y == 5 :
        return True
    
    elif x + y == 5 :
        return True
    
    else :
        return False
    
x = int(input("Enter the 1st integer:"))
y = int(input("Enter the 2nd integer:"))

print("Is ",x, "and ",y, "equal? : ",checkNum(x,y))