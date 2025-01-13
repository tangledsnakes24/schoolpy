""" Sorting Day I: Selection """

# Problem 0: Minimum

def minimum(l):
    smallest_seen = 100000000000000000000000000000000000000
    #while list isnt empty, get smallest element, remove it, add to a new list
    #assume that all elements are greater than 0
    for element in l:
        if element < smallest_seen:
            smallest_seen = element
    return(smallest_seen)

print("Testing Minimum...")
print(minimum([1, 2, 3, 4]))            # 1
print(minimum([2, 3, 4]))               # 2
print(minimum([3, 4]))                  # 3
print(minimum([4]))                     # 4
print()
print("______________________")
# Problem 1: Remove

def remove(element, l):
    flag = False
    new_l = []
    for e in l:
        if ((e != element) or (flag == True)):
                new_l += [e]
        else:
            flag = True
            
    return(new_l)

print("Testing Remove...")
print(remove(1, [1, 2, 3, 4]))          # [2, 3, 4]
print(remove(2, [1, 2, 3, 4]))          # [1, 3, 4]
print(remove(3, [1, 2, 3, 4]))          # [1, 2, 4]
print(remove(4, [1, 2, 3, 4]))          # [1, 2, 3]
print(remove(1, [1, 1, 2, 3, 4]))       # [1, 2, 3, 4]
print()
print("______________________")
# Problem 2: Selection Sort

def selection_sort(l):
    new_l = []
    while len(l) != 0:
        smallest = minimum(l)  #get smallest
        new_l += [smallest] #add to new_l
        l = remove(smallest, l) #remove smallest from list
        
    return(new_l)

print("Testing Selection Sort...")
print(selection_sort([1, 2, 3, 4]))     # [1, 2, 3, 4]
print(selection_sort([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(selection_sort([1, 4, 2, 3]))     # [1, 2, 3, 4]

print(selection_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(selection_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(selection_sort([1, 3, 5, 2, 4]))  # [1, 2, 3, 4, 5]
print()
print("______________________")
# Problem 3: Minimum and Maximum

def min_and_max(l):
    return()

print("Testing Min and Max...")
print(min_and_max([1, 2, 3, 4]))        # (1, 4)
print(min_and_max([4, 3, 2, 1]))        # (1, 4)
print(min_and_max([5, 5, 5, 5]))        # (5, 5)
print()
print("______________________")
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
print("______________________")
