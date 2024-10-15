#Python Exercise
'''
18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
'''

#Solution

# Define a function named "sum_thrice" that takes three integer parameters: x, y, and z
def sum_thrice(x, y, z):
    # Calculate the sum of x, y, and z
    sum = x + y + z

    # Check if x, y, and z are all equal (all three numbers are the same)
    if x == y == z:
        # If they are all equal, triple the sum
        sum = sum * 3
    elif x == y or x == z : 
        # If two of them are equal, double the sum
        sum = sum * 2    

    # Return the final sum
    return sum

numList = input("Enter three numbers (comma delimited):").split(',')


print("Sum is:",sum_thrice(int(numList[0]),int(numList[1]),int(numList[2])))

