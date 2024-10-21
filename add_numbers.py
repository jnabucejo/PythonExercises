#Python Exercise
'''
36. Write a Python program to add two objects if both objects are integers.
'''

# Define a function 'add_numbers' that takes two arguments: a and b.
def add_numbers(a, b):
    # Check if both 'a' and 'b' are integers using the 'isinstance' function.
    if not (isinstance(a, int) and isinstance(b, int)):
    
        # If either 'a' or 'b' is not an integer, return an error message.
        return "Inputs must be integers!"
    # If both 'a' and 'b' are integers, return their sum.
    return a + b

numPair = [int(x) for x in input("Enter a pair of integers (comma delimted): ").split(',')]

print("Sum of ",numPair, "is ",add_numbers(*numPair))
