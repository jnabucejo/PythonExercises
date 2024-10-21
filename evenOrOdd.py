#Python Exercise
'''
21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.
'''

#Solution

def evenOrOdd (num) :
    if num % 2 == 0 :
        print(num,"is Even.")

    else :
        print(num, "is Odd.")


while True:
    try :

        given = int(input("Enter a number (integer): "))
    
    except ValueError :
        print("Invalid input!")
        
    else :
          evenOrOdd(given)
