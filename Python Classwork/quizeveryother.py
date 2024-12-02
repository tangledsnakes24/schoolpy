""" Problem 1: every_other()

Write a function every_other(l) that returns a list with every other element of l.
"""

def every_other(l):
    newlist = []
    for index in range(0, len(l)):
        if l[index] % 2 == 0:
            newlist = newlist + [index]
    return(newlist)

print(every_other([1, 2, 3]))                   # [1, 3]
print(every_other([1, 2, 3, 4]))                # [1, 3]
print(every_other([1, 2, 3, 4, 5]))             # [1, 3, 5]
print(every_other([1, 2, 3, 4, 5, 6]))          # [1, 3, 5]
print(every_other([4, 2, 3, 4, 2, 3]))          #[4, 3, 3]
print(every_other([]))                          #[]

""" Problem 2: odds_then_evens()

Write a function odds_then_evens(l) that returns a new list formed as follows:
    - First, the output should have all the odd elements of the list.
    - After this, the output should have all the even elements of the list.
"""

def odds_then_evens(l):
    templist1 = []
    templist2 = []
    final = []
    for element in l:
        if element % 2 == 0:
            templist1 = templist1 + element
        if element % 2 == 1:
            templist2 = templist2 + element
            
    final = templist1 + templist2
    return(final)

print(odds_then_evens([1, "A", 2]))                 # [1, 2, "A"]
print(odds_then_evens([1, "A", 2, "B"]))            # [1, 2, "A", "B"]
print(odds_then_evens([1, "A", 2, "B", 3]))         # [1, 2, 3, "A", "B"]
print(odds_then_evens([1, "A", 2, "B", 3, "C"]))    # [1, 2, 3, "A", "B", "C"]
#trying to add current element to a list, but forgot how
