""" Project: Collatz Patterns """


""" Problem 1: collatz

Given an integer n, return:
    - 3 * n + 1 if n is odd
    - n / 2 if n is even
Note: To turn a float into an integer (e.g. 2.0 into 2) use the int() function.
"""

def collatz(n):
    if(n%2 == 1):
        n = (3 * n) + 1
    else:
        n = n / 2
    return(int(n))
print("________________________")
print(collatz(1))           # 4: since 1 is odd, we take 3 * 1 + 1
print(collatz(2))           # 1: since 2 is even, we take 2 / 2
print(collatz(3))           # 10: since 3 is odd, we take 3 * 3 + 1
print(collatz(4))           #2
print(collatz(5))           #16
""" Problem 2: collatz_length

Given an integer n, find how many steps it takes for the Collatz Sequence starting at n to reach 1.

"""

def collatz_length(x):
    counter = 0
    while(x != 1):
        if(x % 2 == 0):
            x = (x / 2)
            counter += 1
        elif(x % 2 == 1):
            x = (x * 3) + 1
            counter += 1

    return(counter)
print("_____________________________")
print(collatz_length(1))       # 0 (the sequence is done after no steps at all!)
print(collatz_length(2))       # 1 (the sequence is 2, 1)
print(collatz_length(3))       # 7 (the sequence is 3, 10, 5, 16, 8, 4, 2, 1)
print(collatz_length(4))
print(collatz_length(5))
print(collatz_length(6))
""" Problem 3: longest_collatz_under

Given an integer n, find the length of the longest Collatz Sequence among all numbers less than or equal to n.

"""

def longest_collatz_under(n):
    max_so_far = 0
    for number in range(1, n+1):
        steps = collatz_length(number)
        if(steps > max_so_far):
            max_so_far = steps
    return(max_so_far)
print("_______________________________")
print(longest_collatz_under(1))     # 0
print(longest_collatz_under(2))     # 1
print(longest_collatz_under(3))     # 7
print(longest_collatz_under(4))     # 7
print(longest_collatz_under(5))
print(longest_collatz_under(6))
print(longest_collatz_under(7))



""" Problem 4: collatz_turtle

Given an integer n, draw a "Collatz Curve" corresponding to n.

Specifically, repeat the following until n is 1:
    - if n is odd, turn right 90 degrees and move forward, set n to (3 * n + 1) / 2
    - if n is even, turn left 90 degrees and move forward, set n to n / 2

Use the turtle module, which lets us draw various figures with the following commands:
    - forward(nsteps)
    - left(ndegrees)
    - right(ndegrees)
They each do exactly what you'd expect!


print("_________________________________________________") """
from turtle import *
TK_SILENCE_DEPRECATION = 1

def collatz_turtle(n):
    if(n % 2 == 1):
            right(90)
            forward(100)
            n = (3 * n + 1) / 2
    if( n % 2 == 0):
            left(90)
            forward(100)
            n = n / 2
    return(collatz_turtle)

collatz_turtle(3)
collatz_turtle(4)
collatz_turtle(9)
collatz_turtle(12)