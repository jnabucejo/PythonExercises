#Python Exercise
'''
25. Write a Python program that checks whether a specified value is contained within a group of values.
'''

#Solution

def isPresent (numbers,num) :
    if num in numbers :
        print(num, "is part of ", numbers)
    else :
        print(num, "is not part of ", numbers)


numList = input("Enter a set of numbers (comma delimited):").split(',')
num = input("Enter the number you want to check: ")

isPresent(numList,num)