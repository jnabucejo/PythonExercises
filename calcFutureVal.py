#Python Exercise
'''
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79

FV=P(1+r/n)^nt

where:

P = principal
r = interest rate
n = number of times interest applied per time period
t =	number of time periods elapsed

'''

def calcFV() :
    p = 10000
    r = 3.5/100
    t = 7
    n = 12

    FV = p * ( (1 + r/n ) ** (n * t))

    return FV

print("FV:",round(calcFV(),2))