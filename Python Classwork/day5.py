    
""" Problem 1: Is Prime

Write a function is_prime(x) that returns
    - True if x is prime
    - False if x is composite
You may assume that x is a positive integer greater than 1.
"""
def is_prime(x):
    for possible_divisor in range(2, x):
        if x == 1:
            return(False)
        if x % possible_divisor == 0:
            return(False)
    return(True)
# TESTS GO HERE
print(is_prime(2)) #true
print(is_prime(3))  #true
print(is_prime(6)) # false
print(is_prime(7)) #true
print(is_prime(9))  #false
print(is_prime(1))
print("------------------------------")
def count_factors(x):
    counter = 0
    for possible_divisor in range(1, x+1):
        if x % possible_divisor == 0:
            counter += 1
    return(counter)
# TESTS GO HERE
print(count_factors(2)) #1,2
print(count_factors(3))  #3,1
print(count_factors(6)) # 2,3,6,1
print(count_factors(7)) #7,1
print(count_factors(9))  #3,9,1
print("------------------------------")
#isprime2 is slow asf because it checks all factors, isprime is better because it stops as soon as it finds a number that invalidates it
def is_prime2(x):
    if count_factors(x) == 2:
        return(True)
    else:
        return(False)
print(is_prime2(2))
print(is_prime2(9))
print(is_prime2(12))
print(is_prime(3))
print(is_prime2(6))
print(is_prime2(1))
print("-------------------------------")
""" Problem 2: Count Primes
Write a function count_primes(x) that returns the number of primes less than or equal to x.

You may assume that x is a positive integer greater than 1.
"""
def count_primes(x):
    # CODE GOES HERE
    return()
# TESTS GO HERE

""" Problem 3: Goldbach

The "Goldbach Conjecture" states that all even integers > 2 can be
    written as the sum of two primes.

Write a function goldbach(n) that returns two primes that add to n.

You may assume that n will be an even integer greater than 2.
"""

def goldbach(n):
    for x in range(1, n+1):
        y = n - x
        if is_prime(x) and is_prime(y):
            return(x, y)
        if x > y:
            break  
    return("get rekt goldbach")
# TESTS GO HERE
print(goldbach(4))
print(goldbach(6))
print(goldbach(100))
print(goldbach(12))
print("-----------------------------------------")