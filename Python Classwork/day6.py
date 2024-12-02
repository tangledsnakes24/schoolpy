""" Problem 1: Triangular """

def triangular1(n):
    total = 0
    for k in range(1, n+1):
        total = total + k
    return(total)

print(triangular1(1)) #1
print(triangular1(2)) #3
print(triangular1(3)) #6
print(triangular1(4)) #10
print("___________________________")
def triangular2(n):
    total = 0
    current = 1
    while current <= n:
        total = total + current
        current = current + 1
    return(total)

print(triangular2(1)) #1
print(triangular2(2)) #3
print(triangular2(3)) #6
print(triangular2(4)) #10
print("_________________________________")
""" Problem 2: Even Bump, Odd Drop """

def bump(n):
    return(n + 1)

def drop(n):
    return(n - 1)

def even_bump_odd_drop2(n):
    if (n % 2) == 0:
        n = bump(n)
    elif (n % 2) == 1:
        n = drop(n)
    return(n)
print(even_bump_odd_drop2(1)) #0
print(even_bump_odd_drop2(2)) #3
print(even_bump_odd_drop2(3)) #2
print(even_bump_odd_drop2(4)) #5
print(even_bump_odd_drop2(5)) #4
print("__________________________________")
""" Problem 3: Is Square """
        
def is_square(x):
    for k in range(0, x):
        if x == 0 or x == 1:
            return(True)
        if k * k == x:
            return(True)
    return(False)

print(is_square(4)) #true
print(is_square(5)) #false  
print(is_square(9)) #true   
print(is_square(12)) #fasle
print("__________________________________")
""" Problem 4: Is Sum of Squares """

def is_sum_of_squares(x):
    if x == 0:
        return(True)
    for num in range(0, x + 1):
        first_square = num * num
        second_square = x - first_square
        if second_square < 0:
            break
        print(first_square, second_square)
        if is_square(second_square):
            return(True)
        
    return(False)


print(is_sum_of_squares(0))
print(is_sum_of_squares(1))
print(is_sum_of_squares(2))
print(is_sum_of_squares(3))
print(is_sum_of_squares(4)) #true, 2 and 2
print(is_sum_of_squares(5)) # true 1+4
print(is_sum_of_squares(6)) # false
print(is_sum_of_squares(7)) #false
print(is_sum_of_squares(8)) #true 4+4
print(is_sum_of_squares(9))
print(is_sum_of_squares(10))