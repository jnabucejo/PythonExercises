#Python Exercise
'''
27. Write a Python program that concatenates all elements in a list into a string and returns it.
'''

#Solution

def concat(text) :
    result = ""
    for x in text :
        result = result + x

    print ("Concatenated string: ",result)


inText = input("Enter a series of comma separated item/s: " ).split(',')

concat(inText)