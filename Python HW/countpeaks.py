""" Problem 1: count_peaks()

We say that an element of a list is a "peak" if it is larger than all elements next to it.
Note that the first and last elements of a list can be peaks!

Write a function find_peaks(l) that returns a list with all peaks in a list l, in the original order..

"""

"""
for every element in the list, check if its higher than its neighbors, if yes, add one to the counter, if not, move on to the next element
for element in list:
        prev = element before
        next = element after
        current = current element
        counter = 0
        if current > prev && current > next:
                            counter += 1
    return(counter)
        

"""

def count_peaks(l):
    counter = 0
    for index in range(0, len(l)):
        if len(l) == 1:
            return(0)
        if index == 0:
            curr = l[index]
            next_el = l[index + 1]
            if curr > next_el:
                counter += 1

        elif index == len(l) - 1:
            prev = l[index - 1]
            curr = l[index]
            if curr > prev:
                counter += 1

        else:
            prev = l[index - 1]
            curr = l[index]
            next_el = l[index + 1]
            if curr > prev and curr > next_el:
                counter += 1
    return(counter)

print(count_peaks([2, 1, 2, 1, 2]))             # 3 (all the 2s are peaks)
print(count_peaks([1, 3, 2, 5, 4]))             # 2 (3 and 5 are both peaks)
print(count_peaks([1, 2, 3, 4, 5]))             # 1 (5 is the only peak)
print(count_peaks([]))
print(count_peaks([1]))
