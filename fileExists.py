#Python Exercise
'''
41. Write a Python program to check whether a file exists.
'''

#Solution
import os

filename = input("Enter the name of the file to check:")

if os.path.isfile(filename) :

    print(filename, "exists.")

else :
    print(filename,"does not exist.")