""" Problem 1: Add Evens """
def even_helper(x):
    if(x % 2 == 0):
        return(x)
    else:
        return(0)

    



print("evenhelper")

print(even_helper(2))
print(even_helper(1))
print(even_helper(9))
print("___________________________")
print("addevens")
def add_evens(x, y, z):
    #zero out odd ones, return x+y+z
    x = even_helper(x)
    y = even_helper(y)
    z = even_helper(z)
    return(x + y + z)

print(add_evens(1, 3, 5))       # 0
print(add_evens(1, 3, 6))       # 6
print(add_evens(1, 4, 6))       # 10 = 4 + 6
print(add_evens(2, 4, 6))       # 12 = 2 + 4 + 6
print("___________________________")
"addevens 2"
def addevens2(x, y, z):
    total = 0
    if(x % 2) == 0:
        total = total + x
    if(y % 0) == 0:
        total = total + y
    if(z % 2) == 0:
        total = total + z
    return(total)
print(addevens2(1, 2, 3))
print(addevens2(1, 3, 5))



""" Problem 2: Alternating Sums """

def alternating_sum(n):
    return()

print(alternating_sum(5))       #  3 = 1 - 2 + 3 - 4 + 5
print(alternating_sum(6))       # -3 = 1 - 2 + 3 - 4 + 5 - 6
print(alternating_sum(7))       #  4 = 1 - 2 + 3 - 4 + 5 - 6 + 7
print(alternating_sum(8))       # -4 = 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8
print(alternating_sum(9))       #  5 = 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9

""" Problem 3: Weirdly Alternating Sums """

def weirdly_alternating_sum(n, pos_count):
    return()

print(weirdly_alternating_sum(6, 2))       #  3 = 1 + 2 - 3 + 4 + 5 - 6
print(weirdly_alternating_sum(7, 2))       # 10 = 1 + 2 - 3 + 4 + 5 - 6 + 7
print(weirdly_alternating_sum(8, 2))       # 18 = 1 + 2 - 3 + 4 + 5 - 6 + 7 + 8
print(weirdly_alternating_sum(9, 2))       #  9 = 1 + 2 - 3 + 4 + 5 - 6 + 7 + 8 - 9

print(weirdly_alternating_sum(6, 3))       # 13 = 1 + 2 + 3 - 4 + 5 + 6
print(weirdly_alternating_sum(7, 3))       # 20 = 1 + 2 + 3 - 4 + 5 + 6 + 7
print(weirdly_alternating_sum(8, 3))       # 12 = 1 + 2 + 3 - 4 + 5 + 6 + 7 - 8
print(weirdly_alternating_sum(9, 3))       # 21 = 1 + 2 + 3 - 4 + 5 + 6 + 7 - 8 + 9

""" Problem 4: Round Down Square Root """

def round_down_sqrt(n):
    return()

print(round_down_sqrt(7))       # 2, since 2 < sqrt(7) < sqrt(3)
print(round_down_sqrt(8))       # 2, since 2 < sqrt(8) < sqrt(3)
print(round_down_sqrt(9))       # 3, since sqrt(9) = 3
print(round_down_sqrt(10))      # 3, since 3 < sqrt(10) < 4
print(round_down_sqrt(11))      # 3, since 3 < sqrt(11) < 4