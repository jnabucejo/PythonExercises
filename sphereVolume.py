#Python Exercise
'''
15. Write a  Python program to get the volume of a sphere with the given the radius.

'''

#Solution

#Import pi 
from math import pi

rad = float(input("Enter value for radius: "))

#Volume of sphere = V=4/3πr3
vol = (4 * pi * rad **3)/3

print("Then volume of the sphere with radius = " + str(rad) + " is " + str(vol))