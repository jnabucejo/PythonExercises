#Python Exercise
'''
38. Write a  Python program to solve (x + y) * (x + y).
'''

#Solution

def sumSquare (x,y) :
 
    if not isinstance(x,int) and isinstance(y,int) :
         print("Invalid input!")
        

    else :
       return (x + y) **2


numPair = [int(x) for x in input("Enter a pair of numbers (comma delimited): ").split(',')]

print("The square of the Sum of ",numPair,"is ",sumSquare(*numPair))