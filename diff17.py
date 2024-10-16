#Python Exercise
'''
16. Write a Python program to calculate the difference between a given number and 17.
    If the number is greater than 17, return twice the absolute difference.

'''

#Solution


while True:
    try:
        num = int(input("Enter a number:"))
    
    except ValueError:
        print("Invalid input!")
        continue
    else :
        diff  = num - 17 

        if (num > 17) :
            print("Twice of difference:",diff*2)
        else :
            print ("Difference:", diff)
