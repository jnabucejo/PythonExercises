#Python Exercise
'''
20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
'''

#Solution

def multiply_string (text,n):
    result = ""

    # Use a for loop to repeat the "text" "n" times and concatenate it to the "result"
    for i in range(n):
        result = result + text

    # Return the final "result" string
    return result

inString = input("Input your string: ")
inCtr = int(input("How many times to multiply? "))

print("Output: ",multiply_string(inString,inCtr))