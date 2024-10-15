#Python Exercise
'''
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

'''

#Solution

# Define a function named "near_thousand" that takes an integer parameter "n"
def near_thousand(n):
    # Check if the absolute difference between 1000 and n is less than or equal to 100
    # OR check if the absolute difference between 2000 and n is less than or equal to 100
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

while True:
    try :
        num = int(input("Enter a number:"))

    except ValueError:
        print("Invalid input!")
    
    else:
        print("Answer:",near_thousand(num))