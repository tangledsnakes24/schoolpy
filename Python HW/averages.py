""" 
Problem 1: Average

Write a function average(w, x, y, z) that returns the average of its inputs.

You may assume that all inputs will be integers.
"""
print("average")
def average(w, x, y, z):
    
    return((w+x+y+z)/4)

# TESTS GO HERE
print(average(2,5,5,6))   #should be 4.5
print(average(2,2,2,2))   #should be 2
print(average(1,3,5,7))   #should be 4
print(average(2,5,3,8))   #should be 4.5

"""
Problem 2: Count Odds

Write a function count_odds(x, y, z) that returns the count of odd numbers among its inputs.

You may assume that all inputs will be integers.
"""
print("count_odds")
def count_odds(x, y, z):
    
    return((x%2)+(y%2)+(z%2))

print(count_odds(1,3,5))
print(count_odds(2,4,5))
print(count_odds(1,6,9))