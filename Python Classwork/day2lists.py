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
print(my_list)






print("__________________________")


""" Problem 1: my_max() """

def my_max(l):
    return()

print(my_max([1, 2, 3, 4]))     # 4
print(my_max([4, 3, 2, 1]))     # 4
print(my_max([5, 5, 5, 5]))     # 5



print("___________________")

""" Problem 2: reverse() """

def reverse(l):
    index = len(l) - 1
    reverselists = []
    while index >= 0:
        curr_element = l[index]
        index = index - 1
        reverselists = reverselists + [curr_element]
        


    
    return(reverselists)

print(reverse([1, 2, 3, 4]))     # [4, 3, 2, 1]
print(reverse([4, 3, 2, 1]))     # [1, 2, 3, 4]
print(reverse([5, 5, 5, 5]))     # [5, 5, 5, 5]
print(reverse([]))               #[]

    
print("________________________")




""" Problem 3: duplicate_odds() """

def duplicate_odds(l):
    new_l = []
    for element in l:
        if(element % 2 == 0):
            new_l += [element]
        else:
            new_l += [element, element]
    return(new_l)

print(duplicate_odds([1, 2, 3, 4]))     # [1, 1, 2, 3, 3, 4]
print(duplicate_odds([4, 3, 2, 1]))     # [4, 3, 3, 2, 1, 1]
print(duplicate_odds([5, 5, 5, 5]))     # [5, 5, 5, 5, 5, 5, 5, 5]
print("__________________")
#problem 3.5
def count_odds(l):
    orig_len = len(l)
    new_len = len(duplicate_odds(l))
    return(new_len - orig_len)
print(duplicate_odds([1, 2, 3, 4]))     # [1, 1, 2, 3, 3, 4]
print(duplicate_odds([4, 3, 2, 1]))     # [4, 3, 3, 2, 1, 1]
print(duplicate_odds([5, 5, 5, 5]))     # [5, 5, 5, 5, 5, 5, 5, 5]

print("___________________________")

""" Problem 4: count_ascents() """

def count_ascents(l):
    counter = 0
    for index in range(1, len(l)):
        prev_element = l[index - 1]
        curr_element = l[index]
        if prev_element < curr_element:
            counter += 1
    
    return(counter)

print(count_ascents([1, 2, 3, 4]))         # 3
print(count_ascents([1, 2, 3, 4, 1]))      # 3
print(count_ascents([4, 3, 2, 1]))         # 0
print(count_ascents([5, 5, 5, 5]))         # 0
print("____________________")

#count decents 4.5
def count_decents(l):
    rev_l = reverse(l)
    return(count_ascents(rev_l))
print(count_decents([1, 2, 3, 4]))         # 0
print(count_decents([1, 2, 3, 4, 1]))      # 1
print(count_decents([4, 3, 2, 1]))         # 3
print(count_decents([5, 5, 5, 5]))         # 0
print("____________________")



#count flats:

def count_flats(l):
    if(len == 0):
        return(0)
    total = len(l) - 1
    ascents = count_ascents(l)
    decents = count_decents(l)
    changes = ascents + decents
    
    

    return(total - changes)

print(count_flats([1, 2, 3, 4]))         # 0
print(count_flats([1, 2, 3, 4, 1]))      # 0
print(count_flats([4, 3, 2, 1]))         # 0
print(count_flats([5, 5, 5, 5]))         # 3
print("____________________")



