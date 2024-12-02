""" Problem 1: Sum Evens

Write a program that takes in three integers and adds the even ones together.
"""
"""
def sum_evens(x, y, z):
    if(x % 2 == 0 and y % 2 == 0 and z % 2 == 0):
        return(x + y + z)
    elif(x % 2 == 0 and y % 2 == 0 and z % 2 == 1):
        return(x + y)
    elif(x % 2 == 0 and y % 2 == 1 and z % 2 == 1):
        return(x)
    elif(x % 2 == 1 and y % 2 == 1 and z % 2 == 1):
        return(0)
    elif(x % 2 == 1 and y % 2 == 0 and z % 2 == 0):
        return(y + z)
    elif(x % 2 == 1 and y % 2 == 1 and z % 2 == 0):
        return(z)
    elif(x % 2 == 0 and y % 2 == 1 and z % 2 == 0):
        return(x + z)
  


   

    
    


print(sum_evens(1, 2, 3))   # 2
print(sum_evens(4, 5, 6))   # 10 = 4 + 6
print(sum_evens(1, 3, 5))   #0
print(sum_evens(2, 4, 6))   #12
print(sum_evens(2, 5, 9))   #2"""