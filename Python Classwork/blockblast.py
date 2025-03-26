""" Block Blast """

square = [[0, 0],
          [0, 1],
          [1, 0],
          [1, 1]]

horiz_line = [[0, 0],
              [0, 1],
              [0, 2],
              [0, 3]]

vert_line = [[0, 0],
             [1, 0],
             [2, 0],
             [3, 0]]

elbow1 = [[0, 0],
          [1, 0],
          [1, 1]]

elbow2 = [[0, 0],
          [0, 1],
          [1, 1]]

elbow3 = [[0, 0],
          [0, 1],
          [1, 0]]

elbow4 = [[0, 1],
          [1, 0],
          [1, 1]]

"""
Elbows:

e1     e2     e3     e4
x.     xx     xx     .x           
xx     .x     x.     xx

"""

empty_grid = [[".", ".", ".", "."],
              [".", ".", ".", "."],
              [".", ".", ".", "."],
              [".", ".", ".", "."]]

diag_grid = [["x", ".", ".", "."],
             [".", "x", ".", "."],
             [".", ".", "x", "."],
             [".", ".", ".", "x"]]

def can_place(piece, grid, x, y):
    return()

def place(piece, grid, x, y):
    return()

def clear(grid):
    return()

