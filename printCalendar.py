#Python Exercise
'''
12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''

#Solution

#Import the calendar module
import calendar

mo = int(input("Input month (numeric):"))
yr = int(input("Input year:"))

#Print the calendar
print(calendar.month(yr,mo))

