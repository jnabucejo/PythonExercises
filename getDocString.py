#Python Exercise
'''
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

#Solution

inf=input("Enter a built-in function name:")


funcName=eval(inf)
print(funcName.__doc__)