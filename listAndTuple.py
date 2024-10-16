#Python Exerice
'''
Write a  Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

Sample data: 3, 5, 7, 23
'''
#Solution

items=input("Enter comma separated numbers:")

# Split the 'values' string into a list using commas as separators and store it in the 'list' variable
list1=items.split(',')

# Convert the 'list1' into a tuple and store it in the 'tuple' variable
tuple1=tuple(list1)

#Print the list
print("List",list1)

#Print the tuple
print("Tuple:",tuple1)

