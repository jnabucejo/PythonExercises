#Python Exercise
'''
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
'''


#Solution
filename=input("Enter the filename:")

# Split the 'filename' string into a list using the period (.) as a separator and store it in the 'elements' variable
elements=filename.split('.')

# Print the extension of the file, which is the last element in the 'elements' list
print("The extension of the file is : " + elements[-1])

