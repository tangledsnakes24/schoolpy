""" Sorting Day I: Selection """

# Problem 0: Minimum

def minimum(l):
    return()

print("Testing Minimum...")
print(minimum([1, 2, 3, 4]))            # 1
print(minimum([2, 3, 4]))               # 2
print(minimum([3, 4]))                  # 3
print(minimum([4]))                     # 4
print()

# Problem 1: Remove

def remove(element, l):
    return()

print("Testing Remove...")
print(remove(1, [1, 2, 3, 4]))          # [2, 3, 4]
print(remove(2, [1, 2, 3, 4]))          # [1, 3, 4]
print(remove(3, [1, 2, 3, 4]))          # [1, 2, 4]
print(remove(4, [1, 2, 3, 4]))          # [1, 2, 3]
print()
# Problem 2: Selection Sort

def selection_sort(l):
    return()

print("Testing Selection Sort...")
print(selection_sort([1, 2, 3, 4]))     # [1, 2, 3, 4]
print(selection_sort([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(selection_sort([1, 4, 2, 3]))     # [1, 2, 3, 4]

print(selection_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(selection_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(selection_sort([1, 3, 5, 2, 4]))  # [1, 2, 3, 4, 5]
print()

# Problem 3: Minimum and Maximum

def min_and_max(l):
    return()

print("Testing Min and Max...")
print(min_and_max([1, 2, 3, 4]))        # (1, 4)
print(min_and_max([4, 3, 2, 1]))        # (1, 4)
print(min_and_max([5, 5, 5, 5]))        # (5, 5)
print()

# Problem 4: Double Selection Sort

def double_selection_sort(l):
    return()

print("Testing Double Selection Sort...")
print(double_selection_sort([1, 2, 3, 4]))     # [1, 2, 3, 4]
print(double_selection_sort([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(double_selection_sort([1, 4, 2, 3]))     # [1, 2, 3, 4]

print(double_selection_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(double_selection_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(double_selection_sort([1, 3, 5, 2, 4]))  # [1, 2, 3, 4, 5]
print()
