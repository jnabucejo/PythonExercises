#Python Exercise
'''
14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

'''

#Solution

# Import the 'date' class from the 'datetime' module
from datetime import date

# Convert the inputs to lists
dt1 = input("Enter 1st date in (year, month, day) format:").split(',')
dt2 = input("Enter 2nd date in (year, month, day) format:").split(',')

# Convert the contents of the elements to int to be able to use the date function
f_date = date(int(dt1[0]), int(dt1[1]), int(dt1[2]))
l_date = date(int(dt2[0]), int(dt2[1]), int(dt2[2]))

# Difference between the two dates
diff = l_date - f_date

# Output the days difference 
print("There are " + str(diff.days) + " days between " + str(f_date) + " and " + str(l_date) )

