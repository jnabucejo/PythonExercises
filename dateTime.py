#Python Exercise
'''
3.Write a Python program to display the current date and time.
'''
#Import the 'datetime' module to work with the date and time
import datetime

# Create a datetime object representing the current date and time
now = datetime.datetime.now()

# Use the 'strftime' method to format the datetime object as a string with the desired format
print("Current date and time: ",now.strftime("%Y-%m-%d %H:%M:%S"))
