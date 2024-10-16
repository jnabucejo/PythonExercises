#Python Exercise
'''
24. Write a Python program to test whether a passed letter is a vowel or not.
'''

#Solution

def isVowel(letter) :
    if letter.upper() in 'AEIOU' :
        print(letter,"is a vowel!")
    
    else  :
        print(letter,"is a not a vowel!")


char = input("Enter a letter: ")

isVowel(char)

'''
# Define a function called is_vowel that takes one parameter: char (a character).
def is_vowel(char):
    # Define a string called all_vowels containing all lowercase vowel characters.
    all_vowels = 'aeiou'

    # Check if the input character (char) is present in the all_vowels string.
    return char in all_vowels

char = input("Enter a letter: ")
print(is_vowel(char))
'''