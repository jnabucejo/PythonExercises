#Python Exercise
'''
26. Write a Python program to create a histogram from a given list of integers.
'''

#Solution

def histogram(numList) : 
    
    for num in numList:
        result = ""
        times = num

        while times > 0 :
            result += "*"
            times -= 1

        print(result)


numList = [int(x) for x in input("Enter a list of number (comma delimited): ").split(",")]

histogram(numList)
            