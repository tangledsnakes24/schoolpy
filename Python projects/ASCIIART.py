""" Problem 1: Triangle """
#one more string tool
#multiply strings by intigers
"""
s = ":)"
print(s * 10)
"""
def t(n):
    dotcount = 0
    while dotcount < n:
        dotcount += 1
        print(dotcount * ".")
    print()
    return()

t(3)
t(4)
t(5)

# .       .        .
# ..      ..       ..
# ...     ...      ...
#         ....     ....
#                  .....

""" Problem 2: Pyramid """
#last row is 1*2(n-1) dots
#first row has n-1 spaces before and after dot
#second row has n-2 spaces on each side of 3 dots
#3rd row is n-3 spaces, for 5 dots
#4th row is n-4 spaces, 7 dots
#etc
def p(n):
    counter = 0
    n_spaces = n - 1
    n_dots = 1
    while counter != n:
        print(n_spaces * " " + n_dots * "." + n_spaces * " ")
        n_spaces -= 1
        n_dots += 2
        counter += 1
    
    return()

p(3)
p(4)
p(5)

#                         .
#             .          ...
#   .        ...        .....
#  ...      .....      .......
# .....    .......    .........
""" Problem 2.5: X """
"""
#how many rows      how many x       where is x    how many more . after x
1                   1               index(1)
2                   2               index 2
3                   3               3
4                   4
5                   5
"""


def dia(n):
    for row in range(n):
        
        print("." * row + "x" + "." * (n-row - 1))
    print()
    return()

dia(3)
dia(4)
dia(5)

#             X....
#       X...  .X...
# X..   .X..  ..X..
# .X.   ..X.  ...X.
# ..X   ...X  ....X




""" Problem 3: X """
"""
dots before    dots between   dots after  sum(dots + x's)
0              n-2            0           n
1              n-4              
2              n-8
3              
4
once dots between is 0 or negative, swtich to add dots between



"""
def x(n):
    btwn = n-2
    side_dots = 0
#first few rows, not middle, not bottom
    while btwn > 0:
        print("." * side_dots + "x" + "." * btwn + "x" + "." * side_dots)
        btwn -= 2
        side_dots += 1
    
#middle
    if(n % 2 == 0):
        n_dots = int((n - 2) / 2)
        print(n_dots * "." + "x" + n_dots * ".")
        
    else:    
        #1 x
        n_dots = int((n - 1) / 2)
        print(n_dots * "." + "x" + n_dots * ".")
        btwn = 1
        side_dots += 1


#last rows
    while side_dots >= 0:
        print("." * side_dots + "x" + "." * btwn + "x" + "." * side_dots)
        btwn += 2
        side_dots -= 1
    print()
    return()

x(3)
x(4)
x(5)
x(9)

#             X...X
#       X..X  .X.X.
# X.X   .XX.  ..X..
# .X.   .XX.  .X.X.
# X.X   X..X  X...X

""" Problem 4: Checkerboard """

def c(n, s):
    return()

c(6, 1)
c(3, 2)
c(2, 3)
c(1, 6)

# X.X.X.    XX..XX    XXX...    XXXXXX
# .X.X.X    XX..XX    XXX...    XXXXXX
# X.X.X.    ..XX..    XXX...    XXXXXX
# .X.X.X    ..XX..    ...XXX    XXXXXX
# X.X.X.    XX..XX    ...XXX    XXXXXX
# .X.X.X    XX..XX    ...XXX    XXXXXX 



""" Problem 5: Squares """

def s(n):
    return()

s(3)
s(4)
s(5)

#                .....
#        ....    .XXX.
# ...    .XX.    .X.X.
# .X.    .XX.    .XXX.
# ...    ....    .....
