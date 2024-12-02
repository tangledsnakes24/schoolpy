""" Problem 1: Divisor Sum
The "proper divisors" of a number n are the integers (other than n itself) that divide it perfectly.
For example, 10 has proper divisors 1, 2, and 5,
         and 16 has proper divisors 1, 2, 4, and 8.

Write a program divisor_sum(n) that sums all the proper divisors of n.
"""
#use day5.py functions
def divisors_sum(n):
    counter = 0
    for possible_divisor in range(1, n):
        if n % possible_divisor == 0:
            counter += possible_divisor
    return(counter)

        
print(divisors_sum(10)) # 8 = 1 + 2 + 5
print(divisors_sum(16)) # 15 = 1 + 2 + 4 + 8
print(divisors_sum(12)) #16 = 4, 3, 2, 6, 1
print(divisors_sum(20)) #10, 5, 4, 2, 1 = 22
print(divisors_sum(21)) #7, 3, 1 = 11
print(divisors_sum(14)) # 7, 2, 1 = 10
print(divisors_sum(18)) #9, 6, 3, 2, 1 = 21
# MORE TESTS GO HERE
print("------------------------------------------------")
""" Problem 2: Prime Divisor Sum 
Write a program prime_divisor_sum(n) that sums all the prime proper divisors of n.
"""
def is_prime(x):
    for possible_divisor in range(2, x):
        if x == 1:
            return(False)
        if x % possible_divisor == 0:
            return(False)
    return(True)

def prime_divisors_sum(x):
    counter = 0
    for possible_divisor in range(2, x):
        if x % possible_divisor == 0 and is_prime(possible_divisor) == True:
            counter += possible_divisor
    return(counter)



#tests below
print(prime_divisors_sum(10)) #7
print(prime_divisors_sum(12)) #5
print(prime_divisors_sum(33)) #14
print(prime_divisors_sum(14)) #9
