#Python Exercise
'''
49. Write a  Python program to list all files in a directory.
'''

#Solution

# Import necessary functions and modules from the 'os' library.
from os import listdir
from os.path import isfile, join


def listFiles(dir) :
    # Create a list 'files_list' that contains the names of files in the given directory.
    # It uses a list comprehension to filter files using 'isfile' and 'join' functions.
    files_list = [f for f in listdir(dir) if isfile(join(dir, f))]

    return files_list


dir = input("Enter path of the directory:")

listFiles(dir)

print(listFiles(dir))