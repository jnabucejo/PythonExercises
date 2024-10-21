#Python Exercise
'''
22. Write a Python program to count the number 4 in a given list.
'''                                         

#Solution

givenList = input("Enter a list of numbers (comma delimited): ").split(',')

ctr = 0
for i in givenList : 
    if i == '4' :
        ctr += 1

print ("There is",ctr,"4(s) in the list.")