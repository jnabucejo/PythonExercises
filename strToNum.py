#Python Exercise
'''
48. Write a Python program to parse a string to float or integer.
'''

#Solution

def strToNum(text,type) :
    
    if type == "int" :

       try : 
            return int(float(text))

       except ValueError :
            print("Invalid input!")

    elif type == "float" :
        
        return float(text)

    else :
       print("Invalid input!") 


inString = input("Enter the string to parse:")
ty = input("Enter the type:")

print("Output:",strToNum(inString,ty))

       

