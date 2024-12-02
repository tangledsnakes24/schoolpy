""" Problem 1: add_lists()
Write a function add_lists(l1, l2) that adds two lists element-wise.

Specifically, supppose l1 = [a1, a2, ..., an] and l2 = [b1, b2, ..., bn].
Thus, your function should return [a1 + b1, a2 + b2, ..., an + bn].

You may assume that the two lists will have equal length.
"""
def pad(l, desiredlength, element):
    while len(l) < desiredlength:
        l += [0]

    
    return(l)
print(pad([1, 2, 3], 4, 0))      #1230
print(pad([1, 2, 3], 5, 0))      #12300
print(pad([1, 2, 3], 6, 0))      #123000
print(pad([1], 5, 0))              #10000
print("_____________")
def add_lists(l1, l2):
    if len(l1) > len(l2):
        l2 = pad(l2, len(l1), 0)
    if len(l2) > len(l1):
        l1 = pad(l1, len(l2), 0)
    new_list = []
    for index in range(min(len(l1), len(l2))):
        e1 = l1[index]
        e2 = l2[index]
        s = e1 + e2
        new_list += [s]   
    return(new_list)

print(add_lists([], []))                        # []
print(add_lists([1], [2]))                      # [3]
print(add_lists([1, 2], [3, 4]))                # [4, 6]
print(add_lists([1, 2, 3], [4, 5, 6]))          # [5, 7, 9]
print(add_lists([1, 2, 3, 4], [5, 6, 7, 8]))    # [6, 8, 10, 12]
print(add_lists([3, 4, 5], [2, 4]))             # [5, 8, 5]
print(add_lists([3, 5, 7], [1]))                # [4, 5, 7]
print(add_lists([], [3]))                       # [3]
print("____________________")
""" Problem 2: select()
Write a function select(l, selection_l) that returns a sublist of l as follows:
    - Every occurrance of True in selection_l means the corresponding element
        in l should be included.
    - Every occurrance of False in selection_l means the corresponding element
        in l should NOT be included.

You may assume that the two lists will have equal length.
"""
def select(l, selection_l):
    if len(selection_l) < len(l):
        selection_l = pad(selection_l, len(l), False)
        
    newlist = []
    for index in range(len(l)):
        if selection_l[index] == True:
            newlist = newlist + [l[index]]
    return(newlist)

print(select([1, 2, 3], [True, True, True]))        # [1, 2, 3]
print(select([1, 2, 3], [True, True, False]))       # [1, 2]
print(select([1, 2, 3], [True, False, False]))      # [1]
print(select([1, 2, 3], [False, False, False]))     # []
print(select([1, 2, 3], [True, False]))             #1
print("________________")
""" Problem 3: interweave()
Write a function interweave(l1, l2) that returns a list interweaving l1 and l2.
Specifically, supppose l1 = [a1, a2, ..., an] and l2 = [b1, b2, ..., bn].
Thus, your function should return [a1, b1, a2, b2, ..., an, bn].

Again, you may (not) assume that the two lists will have equal length.
"""

def interweave(l1, l2):
    newerlist = []
    for index in range(len(l1)):
        newerlist += [l1[index], l2[index]]
    return(newerlist)

print(interweave([], []))                       # []
print(interweave([1], ["A"]))                   # [1, "A"]
print(interweave([1, 2], ["A", "B"]))           # [1, "A", 2, "B"]
print(interweave([1, 2, 3], ["A", "B", "C"]))   # [1, "A", 2, "B", 3, "C"]
print("_____________________")
