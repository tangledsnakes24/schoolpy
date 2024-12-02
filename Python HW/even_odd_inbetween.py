""" 
Problem 1: Even Add / Odd Mult

Write a function even_add_odd_mult(x, y) that does the following:

    - If x and y are both even, return their sum.
    - If x and y are both odd, return their product.
    - Otherwise, return 0.

You may assume that x and y will both be positive integers.
"""
print("even_and_odd_mult")
def even_add_odd_mult(x, y):
    if(x % 2 == 0 and y % 2 == 0):
        return(x+y)
    elif(x % 2 == 1 and y % 2 == 1):
        return(x*y)
    else:
        return("0")
    

# TESTS GO HERE
print(even_add_odd_mult(2, 4)) #6
print(even_add_odd_mult(1, 2)) #0
print(even_add_odd_mult(1, 3)) #3
print(even_add_odd_mult(9, 2)) #0


"""
Problem 2: Smallest Even Between

Write a function smallest_even_between(x, y) that returns the smallest even integer between x and y.
If no such integer exists, return 0.


You may assume, however, that both will be positive.
""" 

def smallest_even_between(x, y):
    if(x % 2 == 0):
        return(x+2)
    else:
        return(x+1)

   

# TESTS GO HERE
print(smallest_even_between(2, 5))  #4
print(smallest_even_between(1, 3))  #2
print(smallest_even_between(6, 9))  #8
print(smallest_even_between(1, 5))  #2