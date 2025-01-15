""" Sorting Day II: Insertion and Bubble """

#problem -1
def merge(l1, l2):
    index1 = 0
    index2 = 0
    new_l = []
    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] > l2[index2]:
            new_l += [l2[index2]]
            index2 += 1
        else:
            new_l += [l1[index1]]
            index1 += 1
    if index1 >= len(l1):
        #we have all of l1 already. take my new list, take l2 and add from index
        new_l += l2[index2:]
    else:
        #we have everything from l2
        new_l += l1[index1:]
    return(new_l)

print("testing merge....")
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
    new_l = []
    while len(l) != 0:
        element = l[0]
        new_l = insert(element, new_l)
        l = l[1:]
        
        
    
    return(new_l)

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



#problem 2.5 merge sort

def merge_sort(l, depth):
    print(depth * " " + "I am currently sorting" + str(l))
    if len(l) == 1:
        return(l)
    if len(l) == 2:
        if l[0] > l[1]:
            return([l[1], l[0]])
        else:
            return(l)
    #recursion    
    left = l[:int(len(l)/2)]
    right = l[int(len(l)/2):]
    
    left = merge_sort(left, depth + 1)
    right = merge_sort(right, depth + 1)
    return(merge(left, right))
print("testing merge sort....")
print(merge_sort([1, 2, 3, 4], 0))
print(merge_sort([1, 3, 4, 2], 0))
print(merge_sort([3, 1, 2, 4], 0))
print(merge_sort([1, 4, 3, 2, 5, 6, 7, 8, 12, 11, 10, 45, 20, 35, 36, 23, 42, 52, 32, 73, 69, 13, 39, 29, 43, -1, -100, -2, 5], 0))
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
