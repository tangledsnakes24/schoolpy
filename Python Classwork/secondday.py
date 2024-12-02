x = 3
y = 4

x_bigger_than_y = (x > y)
print(x_bigger_than_y)

x_smaller_than_y = ( x < y)
print(x_smaller_than_y)

x_equal_to_y = (x == y)
print(x_equal_to_y)

x_not_equal_to_y = (x != y)
print(x_not_equal_to_y)
""""
x_is_even
x_is_odd
"""
if (x > y):
    print("xis greater than y")
elif (x == y):
    print("there equal")
else:
    print("x is not greater than y")

def odd_or_even(x):
    if (x % 2 == 0):
        return("even")
    else:
        return("odd")
    

print(odd_or_even(1))    #odd
print(odd_or_even(2))    #even
print(odd_or_even(3))    #odd
print(odd_or_even(4))    #even
print(odd_or_even(5))    #odd

def odds_or_evens(x, y):
    if(x % 2 == 1):     #if x is odd
        if(y % 2 == 1):   #if y is odd
            return("odds")  
        else:
            return("odd and even")
    else:
        if (y % 2 == 1):
            return("even and odd")
        else:
            return("evens")
def odd_or_even2(x, y):
    if( x % 2 == 1 and y % 2 == 1):
        return("odds")
    if( x % 2 == 0 and y % 2 == 0):
        return("evens")
    else:
        return("even and odd")


print(odd_or_even2(3, 3)) #odds
print(odd_or_even2(3, 4)) #odd and even
print(odd_or_even2(4, 4))   #evens
print(odd_or_even2(4, 5))  #even and odd



print(odds_or_evens(3, 3)) #odds
print(odds_or_evens(3, 4)) #odd and even
print(odds_or_evens(4, 4))   #evens
print(odds_or_evens(4, 5))  #even and odd

def maximum(x, y):
    if(x - y > 0):
        return(x)
   
    else:
        return(y)
   



print(maximum(2, 9)) #9
print(maximum(1, 3)) #3
print(maximum(2, 8)) #8

def fizzbuzz(x):
    if(x % 3 == 0 and x % 5 == 0):
        return("fizzbuz")
    elif(x % 3 == 0):
        return("fizz")

    elif(x % 3 == 1 and x % 5 == 1):
        return(x)
    
    else:
        return("buzz")
    
    
print(fizzbuzz(3)) #fizz
print(fizzbuzz(5)) #buzz
print(fizzbuzz(15)) #fizzbuzz
print(fizzbuzz(7)) #4