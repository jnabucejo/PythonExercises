#Python Exercise
'''
4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

#Solution

from math import pi

def circleArea(radius):
    area = pi * radius **2

    return area


try:

    r= float(input("Enter radius:"))
    print("Area of the circle = ",circleArea(r))
    
except ValueError:
    print("Invalid value for radius!")





