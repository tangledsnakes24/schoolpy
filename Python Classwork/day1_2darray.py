
""" 2D Arrays """

g1 = [[1, 2],
      [3, 4]]

g2 = [["x", "o", "x"],
      ["x", "o", "o"],
      ["x", ".", "."]]

g3 = [[True, True, True, False, True, True, True, False, True],
      [True, False, True, True, True, False, True, True, True]]
print(g1[1])
print(g1[0][0])
# Problem 1: Fetch

def fetch(grid, x, y):
    return()

print("Testing Fetch...")

print(fetch(g1, 0, 0))      # 1
print(fetch(g1, 0, 1))      # 3
print(fetch(g1, 1, 0))      # 2
print(fetch(g1, 1, 1))      # 4
print(fetch(g1, 2, 2))      # None

print(fetch(g2, -1, -1))    # None
print(fetch(g2, 0, 0))      # "x"
print(fetch(g2, 1, 1))      # "o"
print(fetch(g2, 2, 2))      # "."
print(fetch(g2, 3, 3))      # None

# Problem 2: Count Neighbors

m1 = [["?", ".", "."],
      ["X", "?", "X"],
      [".", "?", "X"],
      [".", "?", "."],
      ["X", "?", "?"]]

def count_neighbors(grid, x, y):
    return()

print(count_neighbors(m1, 0, 0))        # 1
print(count_neighbors(m1, 1, 1))        # 3
print(count_neighbors(m1, 1, 2))        # 3
print(count_neighbors(m1, 1, 3))        # 2
print(count_neighbors(m1, 1, 4))        # 1
print(count_neighbors(m1, 2, 4))        # 0


# Problem 3: Times Table

def times_table(max_x, max_y):
    return()

print(times_table(2, 2))            # [[1, 2],
                                    #  [2, 4]]

print(times_table(3, 3))            # [[1, 2, 3],
                                    #  [2, 4, 6],
                                    #  [3, 6, 9]]

print(times_table(4, 6))            # [[1,  2,  3,  4],
                                    #  [2,  4,  6,  8],
                                    #  [3,  6,  9,  12],
                                    #  [4,  8,  12, 16],
                                    #  [5,  10, 15, 20],
                                    #  [6,  12, 18, 24]]

# Problem 4: Back and Forth

def back_and_forth(max_x, max_y):
    return()

print(back_and_forth(2, 2))         # [[1, 2],
                                    #  [4, 3]]

print(back_and_forth(3, 3))         # [[1, 2, 3],
                                    #  [6, 5, 4],
                                    #  [7, 8, 9]]

print(back_and_forth(4, 5))         # [[1,  2,  3,  4],
                                    #  [8,  7,  6,  5],
                                    #  [9,  10, 11, 12],
                                    #  [16, 15, 14, 13],
                                    #  [17, 18, 19, 20],
                                    #  [24, 23, 22, 21]]

