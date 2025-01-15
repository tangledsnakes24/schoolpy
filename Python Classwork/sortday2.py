""" Sorting Day II: Insertion and Bubble """

#problem -1
def merge(l1, l2):
    index1 = 0
    index2 = 0
    new_l = []
    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] > l2[index2]:
            new_l += l2[index2]
            index2 += 1
        else:
            new_l += l1[index1]
            index1 += 1
            
    return(new_l)



print(merge([1, 3, 5], [2, 4])) # 12345
print(merge([1], [2, 3, 4, 5])) #12345
print(merge([1, 5], [2, 3, 4])) #12345
print(merge([1, 2, 3, 4], [5])) #12345
# Problem 0: Insert
#while list isnt empty:
#remove 0th element of l
#insert it into new_l in correct position
#repeat until sorted
#assume l is in ascendng order
def insert(element, l):
    return(merge([element], l))

print("Testing Insert...")
print(insert(1, [2, 3, 4]))            # [1, 2, 3, 4]
print(insert(2, [1, 3, 4]))            # [1, 2, 3, 4]
print(insert(3, [1, 2, 4]))            # [1, 2, 3, 4]
print(insert(4, [1, 2, 3]))            # [1, 2, 3, 4]
print()
print("____________________________")

# Problem 1: Insertion Sort

def insertion_sort(l):
    return()

print("Testing Insertion Sort...")

print(insertion_sort([1, 2, 3, 4]))     # [1, 2, 3, 4]
print(insertion_sort([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(insertion_sort([1, 3, 2, 4]))     # [1, 2, 3, 4]

print(insertion_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(insertion_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(insertion_sort([2, 4, 1, 3, 5]))  # [1, 2, 3, 4, 5]
print()
print("____________________________")

# Problem 2: Swap

def swap(l, pos1, pos2):
    return()

print("Testing Swap...")
print(swap([2, 1, 3, 4], 0, 1))         # [1, 2, 3, 4]
print(swap([1, 3, 2, 4], 1, 2))         # [1, 2, 3, 4]
print(swap([1, 2, 4, 3], 2, 3))         # [1, 2, 3, 4]
print()
print("____________________________")

# Problem 3: Bubble Sort

def bubble_sort(l):
    return()

print("Testing Bubble Sort...")

print(bubble_sort([1, 2, 3, 4]))     # [1, 2, 3, 4]
print(bubble_sort([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(bubble_sort([1, 3, 2, 4]))     # [1, 2, 3, 4]

print(bubble_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(bubble_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(bubble_sort([2, 4, 1, 3, 5]))  # [1, 2, 3, 4, 5]
print()
print("____________________________")
