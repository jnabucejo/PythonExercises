#Python Exercise
'''
31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

GCD (a, b) = (a × b)/ LCM (a, b)
'''

#Solution

from getLCM import lcm

def GCD(a,b):

    gcd = a * b /lcm(a,b)


    return int(gcd)

x = input("Enter your first integer: ")
y = input("Enter your second integer: ")

print("GCD of", x,"&",y, "is ", GCD(int(x),int(y)))