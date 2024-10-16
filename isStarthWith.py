#Python Exercise
'''
19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
 Return the string unchanged if the given string already begins with "Is".
'''

#Solution

inString = input("Enter your string: ")

if inString.upper().startswith("IS") :
    print("Output: ",inString)

else : 
    newString = "Is" + inString
    print("Output: ",newString)