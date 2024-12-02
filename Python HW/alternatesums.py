""" Problem 1: Alternating Sums
To sum the first n integers, we add 1 + 2 + 3 + ... + n.
To get the "alternating sum" of the first n integers, we replace every other plus with a minus.
This gives us the sum 1 - 2 + 3 - 4 + 5 - 6 + ... + n (if n is odd),
                   or 1 - 2 + 3 - 4 + 5 - 6 + ... - n (if n is even).

Write a program alternating_sum(n) that calculates the alternating sum of the first n integers.
"""
print("------------------------")
def alternating_sum(n):
    num1 = 0
    for x in range (1, n+1):
        if(x % 2 == 0):
            num1 = num1 - x
        else:
            num1 = num1 + x            
    return(num1)

print(alternating_sum(4))   # 1-2+3-4 = -2
print(alternating_sum(5))   # 1-2+3-4+5 = 3
print(alternating_sum(6))   # -3
# MORE TESTS GO HERE
print("------------------------")

""" Problem 2: Weirdly Alternating Sums
Instead of always switching between plus and minus, we can consider other patterns.
We'll still work our way up from 1 to n, but now we'll vary the number of pluses we have before each minus.

Write a program weirdly_alternating_sum(n, pos_count) that does this.
    - The input n tells you how many summands you should have total.
    - The input pos_count tells you how many positive summands you should include before each negative.

You may assume that both inputs will be positive integers.    
"""

def weirdly_alternating_sum(n, pos_count):
    num2 = 0
    counter = 0
    for x in range(1, n+1):
        if(counter < pos_count):
            num2 = num2 + x
            counter = counter + 1
        else:
            num2 = num2 - x
            counter = 0
    return(num2)

print(weirdly_alternating_sum(6, 2))       # 3 = 1 + 2 - 3 + 4 + 5 - 6
print(weirdly_alternating_sum(7, 2))       # 10 = 1 + 2 - 3 + 4 + 5 - 6 + 7
print(weirdly_alternating_sum(4, 8))       # 1+2+3+4 = 10 
print(weirdly_alternating_sum(15, 5))      # 1+2+3+4+5-6+7+8+9+10-11+12+13+14+15



   