""" Problem 1: Sum Evens and Odds
Write a function sum_evens_odds(l) that returns a list with two elements.

    - The first element should contain the sum of all odd elements of l
    - The second element should contain the sum of all even elements of l.

You may assume that all elements of l will be positive integers.
"""

def sum_evens_odds(l):
    odd = 0
    even = 0
    for element in l:
        if(element % 2 == 0):
            even += element
        elif(element % 2 == 1):
            odd += element
        
    return([odd, even])

print(sum_evens_odds([1, 2, 3, 4]))         # [4, 6]
print(sum_evens_odds([3, 3, 3, 5]))         # [14, 0]
print(sum_evens_odds([1, 3, 5, 7]))         #[16, 0]
print(sum_evens_odds([1, 4, 8, 9]))         #[10, 12]
