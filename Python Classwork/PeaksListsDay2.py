""" More on Lists """

# Recap:

my_list = [1, 2, 3, 4]

print(my_list[0])
print(my_list[3])

for element in my_list:
    if element % 2 == 0:
        print("even")
    else:
        print("odd")

my_list = my_list + [5]
print("___________________________")
print(my_list)
print("_________________________")

#add lists, order matters, add in order of where you want each element to appear
#problem 0, insert


def insert(l, insert, pos):
    if pos > len(l):
        return(None)
    if pos == len(l):
        return(l + [insert])
    new_l = []
    for index in range(0, len(l)):
        if index == pos:
            new_l = new_l + [insert]
            
        current_element = l[index]
        new_l = new_l + [current_element]
    return(new_l)

print("______________________________")

print(insert([1, 2], 3, 2))
print(insert([1, 2], 3, 1))
print(insert([1, 2], 3, 0))
print(insert([1, 2], 3, 4))

print("___________________________")



""" Problem 1: my_max() """

def my_max(l):
    if len(l) == 0:
        return(None)
    counter = l[0]
    for element in l:
        if element > counter:
            counter = element
        



    
    return(counter)
print("________________________________________")
print(my_max([1, 2, 3, 4]))     # 4
print(my_max([4, 3, 2, 1]))     # 4
print(my_max([5, 5, 5, 5]))     # 5
print(my_max([-1, -2, -3]))     # -1
print(my_max([]))

print("__________________________")



""" Problem 2: reverse() """

def reverse(l):
    return()
print("_______________________________")
print(reverse([1, 2, 3, 4]))     # [4, 3, 2, 1]
print(reverse([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(reverse([5, 5, 5, 5]))     # [5, 5, 5, 5]
print("________________________________")




""" Problem 3: duplicate_odds() """

def duplicate_odds(l):
    return()
print("________________________________")
print(duplicate_odds([1, 2, 3, 4]))     # [1, 1, 2, 3, 3, 4]
print(duplicate_odds([4, 3, 2, 1]))     # [4, 3, 3, 2, 1, 1]
print(duplicate_odds([5, 5, 5, 5]))     # [5, 5, 5, 5, 5, 5, 5, 5]
print("________________________________")




""" Problem 4: count_ascents() """

def count_ascents(l):
    return()
print("________________________________")
print(duplicate_odds([1, 2, 3, 4]))         # 3
print(duplicate_odds([1, 2, 3, 4, 1]))      # 3
print(duplicate_odds([4, 3, 2, 1]))         # 0
print(duplicate_odds([5, 5, 5, 5]))         # 0
print("________________________________")
