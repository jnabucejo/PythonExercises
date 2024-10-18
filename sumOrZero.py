#Python Exercise
'''
33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.'
'''

#Solution

def isTheSame(numbers):

    y = 0
    tot = 0
    for x in numbers :
        if y == x :
            tot = 0
            break
        else :
            y = x
            tot += x

    print("Sum:",tot)

numList = [int(x) for x in input("Enter a list of 3 numbers (comma delimited): ").split(",")]

isTheSame(numList)
