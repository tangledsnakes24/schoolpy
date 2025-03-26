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

upwardt = [[1, 0],
           [0, 1],
           [1, 1],
           [1, 2]]

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

def can_place(piece, grid, x_ref, y_ref):
    for coord in piece:
        x_disp = coord[0]
        y_disp = coord[1]
        x_coord = x_ref + x_disp
        y_coord = y_ref + y_disp

        if y_coord >= 0 and y_coord < len(grid):
            row = grid[y_coord]
            if x_coord >= 0 and x_coord < len(row):
                element = row[x_coord]
                if element == "x":
                    print("crashes into x")
                    return(False)
            else:
                print("goes off an edge")
                return(False)
        else:
            print("goes off top or bottom")
            return(False)
    return(True)
print(can_place(upwardt, empty_grid, 0, 0)) #true
print(can_place(upwardt, empty_grid, 1, 2)) #true
print(can_place(upwardt, empty_grid, 2, 0)) #false
print(can_place(upwardt, empty_grid, 1, 3)) #false
print(can_place(upwardt, empty_grid, -1, -1)) #false
print(can_place(upwardt, diag_grid, 0, 2))  #true
print(can_place(upwardt, diag_grid, 2, 0))  #false
print(can_place(upwardt, diag_grid, 1, 1))  #false
print(can_place(upwardt, diag_grid, 2, 2))  #false

def place(piece, grid, x, y):
    return()

def clear(grid):
    return()

