#Python Exercise
''''
29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}

'''

#Solution

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def isPresent(list1,list2) :
    result=[]
    for x in list1 :
        if x not in list2 :
            result.append(x)
    
    print(set(result))

isPresent(color_list_1,color_list_2)