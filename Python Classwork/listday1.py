"""Lists in Python """


# Three DIFFERENT lists!

l1 = [1, 2, 3]
l2 = [3, 2, 1]
l3 = [1, 1, 1, 2, 2, 3]

# "Indexing" into lists
print(l3[4])


# Looping over lists
for element in l3:
    print(element)


# Adding things to lists
print(l1 + l2) #123321
l1 = l1 + [4] #to add element use *listname* = *listname* + [element]
print(l1)

""" Problem 1: list_sum() """

def list_sum(l):
    total = 0
    for number in l:
        total += number
    return(total)

print(list_sum([]))                 # 0
print(list_sum([1]))                # 1
print(list_sum([1, 2]))             # 3
print(list_sum([1, 2, 3]))          # 6
print(list_sum([1, 2, 3, 4]))       # 10


""" Problem 2: count_appearances() """

def count_appearances(l, e):
    total1 = 0
    for number in l:
        if number == e:
            total1 += 1
    return(total1)

print(count_appearances([1, 2, 3], 1))       # 1
print(count_appearances([1, 2, 3], 2))       # 1
print(count_appearances([1, 2, 3], 3))       # 1
print(count_appearances([1, 2, 3], 4))       # 0
print(count_appearances([1, 1, 2], 1))       # 2

""" Problem 3: remove_appearances() """

def remove_appearances(l, e):
    new_l = []
    for element in l:
        if element != e:
            new_l = new_l + [element]
    return(new_l)

print(remove_appearances([1, 2, 3], 1))       # [2, 3]
print(remove_appearances([1, 2, 3], 2))       # [1, 3]
print(remove_appearances([1, 2, 3], 3))       # [1, 2]
print(remove_appearances([1, 2, 3], 4))       # [1, 2, 3]
print(remove_appearances([1, 1, 2], 1))       # [2]

""" Problem 4: double_all() """

def double_all(l):
    newlist1 = []
    for element in l:
        newlist1 = newlist1 + [2 * element]
    return(newlist1)
print("_______________")
print(double_all([]))               # []
print(double_all([1]))              # [2]
print(double_all([1, 2]))           # [2, 4]
print(double_all([1, 2, 3]))        # [2, 4, 6]
print(double_all([1, 2, 3, 4]))     # [2, 4, 6, 8]
