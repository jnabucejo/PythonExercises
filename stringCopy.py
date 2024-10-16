#Python Exercise
'''
23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
 Return n copies of the whole string if the length is less than 2.
'''

#Solution

def stringCopy(text, num) :
    flen = 2
    if flen > len(text)  : 
        flen = len(text)

    subString = text[:flen]
    newText = ""

    
    for i in range(num):
        newText = newText + subString
    return newText

givenString = input("Enter a string: ")
giventCtr = int(input("Enter a number:"))

print("Output:",stringCopy(givenString,giventCtr))

